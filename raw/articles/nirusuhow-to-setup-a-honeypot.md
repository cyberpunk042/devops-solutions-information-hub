# Nirusu/how-to-setup-a-honeypot

Source: https://github.com/Nirusu/how-to-setup-a-honeypot
Ingested: 2026-05-04
Type: documentation

---

# README

# Building a TLS-compatible Honeypot 
This guide illustrates how to set up a honeypot that, next to unencrypted network traffic, is also capable of decrypting TLS traffic with the help of [PolarProxy](https://www.netresec.com/?page=PolarProxy). It is part of my master's thesis that uses a version of this setup to analyze attacks on specific HTTP(S) web-based applications.

![Illustration of the setup](images/setup.svg)

Note that this documentation is mostly a recollection and recreation of the events from the initial setup from the honeypot used in my thesis, and I have not tested them thoroughly again when writing this post. Therefore, if you find any mistake, feel free to open an issue or pull request or let me know otherwise!

## Infrastructure
For this setup, we use two servers. The first server, called the *Gateway Server*, runs an installation of Ubuntu 20.04. It is has two network interfaces, with one connected to the internet and assigned a /24 subnet, and the other connected to the other server.

The second server, called the *Proxmox Server*, runs [Proxmox VE](https://www.proxmox.com/en/proxmox-ve), a virtualization environment that allows us to run VMs. It is connected with an Ethernet cable to the first server but not directly to the internet. 

Usually, getting access to a /24 subnet can be quite expensive. The main reason a /24 subnet is used in this tutorial is that the project was initially done at a university with larger subnets available for research. However, given that not all IP addresses of the subnet are needed, it can also be done with smaller subnets or multiple independent IP addresses. To replicate this setup on typical cloud providers, buying multiple IP addresses and running a VPC for the internal connection between the two servers should also work.

## Initial Networking Setup
For demonstration purposes, we use the 198.51.100.0/24 test IPv4 address range as an example for our /24 subnet.

### Network Interface Configuration
The general idea of the honeypot networking is that one external IP address maps to one VM. To achieve this, we manually define the external IP addresses and also define all possible VLANs, ranging from 2-255. All VLANs use a /30 subnet, with the purpose being that only the Gateway Server and a VM can reside inside a VLAN.

On the Gateway Server, we use Netplan to configure the network. `enp4s0f0` is the network interface connected to the internet and `enp7s0f0` is the network interface that connects both servers internally.

An example configuration can look like this, with the repetitive VLAN definitions ranging to `vlan.255` cut out (a full version can be found in [netplan.yaml](netplan.yaml)):

```yaml
network:
  version: 2
  ethernets:
    enp4s0f0:
      addresses: 
        - 198.51.100.42/24 # Gateway server external IP address 
        - 198.51.100.4/24 # One Honeypot Service
        - 198.51.100.12/24 # Another Honeypot Service
      gateway4: 198.51.100.1
      dhcp4: false
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
    enp7s0f0:
      dhcp4: false
      addresses: [192.168.1.1/30]
  vlans:
    vlan.2:
      id: 2
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.2.1/30]
    vlan.3:
      id: 3
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.3.1/30]
    ...
```

It is possible to define the whole subnet for the external IP addresses at one go instead of each IP defined manually. However, given that we did not want to route traffic to our machine for unassigned IP addresses, we decided to opt for the latter option. This should also allow an easier adaption in case a whole /24 subnet is not available, but rather multiple IP addresses. These can be defined in the same way in this configuration.

### Firewall
By default, we do not want to allow any incoming traffic to either the Gateway Server or the VMs that is not intended by us. Traffic to the Gateway Server itself is considered as `INPUT` in iptables, whereas traffic for the VMs is considered as `FORWARD`. 

Before we drop all access by default, we need to ensure we still keep access before applying the firewall rules. First, we set an allowed subnet from which we can continue to access everything:

```bash
sudo iptables -A INPUT -i enp4s0f0 -s 192.0.2.0/24 -j ACCEPT
```

Note that `192.0.2.0/24` is used as a placeholder here to specify a subnet that is allowed to access the Proxmox management interface and SSH. It can be replaced with another specific subnet or IP address that is allowed to access these services. 

Then, we need to ensure that outgoing traffic is still allowed when initiated from an allowed `INPUT` or `FORWARD` rule:

```bash
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

After we specifically allowed incoming traffic from a trusted network and outgoing traffic back to it to ensure we do not lock ourselves out, we can eventually drop all other traffic by default:

```bash
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
```

Additionally, we can allow traffic for loopback traffic by default:
```bash
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
```

### Access to the Proxmox Server
The Proxmox installation on the second server is configured with the IP address 192.168.1.2 and runs outside of a VLAN. To gain access to SSH and the Proxmox management interface on the second server, we setup the following `iptable` rules on the Gateway Server that offer access to both services under the same external IP address as the Gateway Server:
```bash
# Proxmox management interface
sudo iptables -A FORWARD -s 192.0.2.0/24 -d 192.168.1.2 -p tcp --dport 8006 -j ACCEPT
sudo iptables -A FORWARD -s 192.168.1.2 -d 192.0.2.0/24 -p tcp --sport 8006 -j ACCEPT
sudo iptables -A PREROUTING -t nat -p tcp -s 192.0.2.0/24  --dport 8006 -j DNAT --to-destination 192.168.1.2:8006

# SSH
sudo iptables -A PREROUTING -t nat -p tcp -s 192.0.2.0/24  --dport 2222 -j DNAT --to-destination 192.168.1.2:22
sudo iptables -A FORWARD -s 192.0.2.0/24 -d 192.168.1.2 -p tcp --dport 22 -j ACCEPT
sudo iptables -A FORWARD -d 192.0.2.0/24 -p tcp --sport 22 -j ACCEPT
```

The same note as above applies for `192.0.2.0/24`.

In addition, we still want Proxmox itself to be able to reach the internet for updates. Therefore, we add the additional following rules to allow Proxmox to masquerade its traffic under the same external IP address as the Gateway Server:

```bash
sudo iptables -t nat -A POSTROUTING -s 192.168.1.2 -j MASQUERADE
sudo iptables -A FORWARD -d 192.168.1.2 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -s 192.168.1.2 -o enp4s0f0 -j ACCEPT
```

### Configuring VLAN support for Proxmox
In order to eventually be able to assign VLANs per VM, we need to do some additional networking configuration in Proxmox.
Assuming that previously, the Proxmox network configuration was done over a **Network Device** in Proxmox, we need to make some changes to be able to define VLANs on the side of the Proxmox Server. 

Under the "Networking" tap in Proxmox, we need to create a **Linux Bridge** and a **Linux VLAN** that uses the newly created bridge device for VLAN 1. 

The **Linux Bridge** itself needs to be configured as VLAN-aware, with the Bridge ports being the Network Device for the internal connection between the two servers, presumably the same network device configured before. In our case, similar to the Gateway Server, this is `enp7s0f0`.

<img src="images/bridge.png" alt="Proxmox vmbr1 Linux Bridge configuration" width="500"/>

Then, for the **Linux VLAN**, VLAN 1 holds the same configuration as the Network Device did before and is required to keep being able to be still able to reach the server under the same internal IP address over the Gateway Server as before. The screenshots below show the setting we used for each device, with vmbr1 being the Linux Bridge and vmbr1.1 being the Linux VLAN:

<img src="images/vlan-1.png" alt="Proxmox vmbr1.1 Linux VLAN configuration" width="500"/>


Afterward, we can remove the IP address from the Network Device and apply the changes. 

In total, the network configuration should look similar to this (with disregard to the inactive network interfaces shown):

<img src="images/network-list.png" alt="List of all network devices in Proxmox" width="600"/>

## VM Setup
With the initial setup being done, we can now create VLANs that use the newly created Linux Bridge device `vmbr1` and assign a VLAN tag to use for the VM. For example, for a VM that, under the /24 subnet example, is supposed to be reachable under 198.51.100.150 from the Internet or 192.168.150.2 internally from the Gateway Server, we would use the VLAN tag 150. 

<img src="images/create-new-vm.png" alt="Proxmox 'Network' tab during VM creation" width="500"/>

Additionally, if rate limiting is desired in case any malicious services are running when a VM gets infected, it can also be configured under the same networking tab directly in Proxmox.

Before we install any operating system inside the VM, it makes sense to create the networking rules for a single VM before we install any VM. Here, we distinct between VMs where we do not want to intercept any incoming TLS traffic, and VMs for which we do.

### Non-TLS Traffic
For VMs not running any TLS-enabled services, we create the following rules:

* Incoming traffic for a specific external IP address is translated to the internal IP address of the respective VM (DNAT)
* Outgoing traffic from a specific VM is translated to its specific external IP address (SNAT)
* Incoming traffic is only allowed for a specific port and already established connections (important to keep outgoing traffic alive)
* Outgoing traffic is fully allowed, except to other VMs

For `iptables`, this can be translated into the following rules:

```bash
sudo iptables -t nat -A PREROUTING -d 198.51.100.XX/32 -j DNAT --to-destination 192.168.XX.2
sudo iptables -t nat -A POSTROUTING -s 192.168.XX.2/32 -j SNAT --to-source 198.51.100.XX
sudo iptables -A FORWARD -s 192.168.XX.2 -o enp4s0f0 -j ACCEPT
sudo iptables -A FORWARD -d 192.168.XX.2 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -d 192.168.XX.2 -p tcp --dport YY -m iprange ! --src-range 192.168.0.0-192.168.255.255 -j ACCEPT

# In case Docker is installed, forbid traffic to Docker networks by default
sudo iptables -I DOCKER-USER -s 192.168.XX.2 -d 172.16.0.0/12 -m state --state NEW -j DROP 
```

XX is a place holder for the VLAN tag, and YY the port of a service we want to allow for the outside. 


### TLS Traffic
When we want to intercept incoming TLS traffic with the help of [PolarProxy](https://www.netresec.com/?page=PolarProxy), it will be running on the Gateway Server itself, and not inside the VM. Therefore, we need to create an exception for the routing rules that incoming ports expecting TLS are not directly forwarded to the VM:

```bash
sudo iptables -t nat -A PREROUTING -d 198.51.100.XX/32 -j DNAT -p tcp --to-destination 192.168.XX.2 ! --dport YY
sudo iptables -t nat -A PREROUTING -d 198.51.100.XX/32 -j DNAT --to-destination 192.168.XX.2 ! -p tcp
sudo iptables -t nat -A POSTROUTING -s 192.168.XX.2/32 -j SNAT --to-source 198.51.100.XX
sudo iptables -A FORWARD -s 192.168.XX.2 -o enp4s0f0 -j ACCEPT
sudo iptables -A FORWARD -d 192.168.XX.2 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -d 198.51.100.XX -p tcp --dport YY -m iprange ! --src-range 192.168.0.0-192.168.255.255 -j ACCEPT

# In case Docker is installed, forbid traffic to Docker networks by default
sudo iptables -I DOCKER-USER -s 192.168.XX.2 -d 172.16.0.0/12 -m state --state NEW -j DROP 
```

Here, we instruct the system not to forward TCP port YY to the VM directly, but all other TCP and UDP traffic is passed through, similar to the Non-TLS traffic. 

### VM Network Configuration
With these rules set in place, we can install the operating system inside the VM. For the network configuration, we use a static configuration with the following settings:

* **Subnet**: 192.168.XX.0/30 (**Subnet Mask**: 255.255.255.252)
* **IP Address**: 192.168.XX.2
* **Gateway**: 192.168.XX.1
* **DNS**: 8.8.8.8, 8.8.4.4 (replaceable with other public DNS servers)

An example configuration for Ubuntu 20.04 with the VLAN tag 150 is shown here:
<img src="images/vm-network-config.png" alt="Ubuntu 20.04 network configuration dialog" width="500"/>

After installation, the VM should be able to access the internet. The desired honeypot service running under port YY defined with the iptables rules above can now be installed and, in case of a non-TLS port, should be exposed to the internet after installation. For a TLS port, we need to start PolarProxy in the next step before it is eventually exposed to the internet.

## Capturing Network Traffic
Now that we have our service up and running, we can start by capturing the network traffic from our Gateway Server. Here, we take a look at the global traffic (useful for unencrypted traffic) and how to capture the TLS traffic for the ports we made an exemption before.
### Complete Network Traffic
To capture the global traffic of a VM, we can leverage [TShark](https://www.wireshark.org/docs/man-pages/tshark.html), which is a Terminal version of Wireshark. 

After installation, we can capture the network traffic of the VM by telling TShark to capture traffic on the network interface `vlan.XX`, with XX being the VLAN tag.

As an example, to capture traffic for the VM on VLAN tag 150, we can use the following command:
```bash
tshark -i vlan.150 -w /mnt/data/pcaps/vlan150.pcap
```

When the capture is running for a longer while, or when the VM is experiencing high traffic, it can result in either dropped packages or very large PCAP files that are hard to analyze in tools like Wireshark. Therefore, a good idea is to increase the capture buffer size with `-B`, and the ring buffer size with `-b` which automatically rotates to a new PCAP file.

For example, using a capture buffer size of 256 MB and a maximum PCAP size of 1 GB before rotating would look like this:

```bash
tshark -B 256 -b filesize:1000000 -w /mnt/data/pcaps/vlan150.pcap
```

### TLS Traffic
In order to host TLS service and being able to capture incoming traffic, we now leverage PolarProxy running on the Gateway Server. First, after downloading and unpacking the most recent version from the [website](https://www.netresec.com/?page=PolarProxy), we add the capability to allow PolarProxy to listen on ports <1024 without requiring to run it as root or with sudo:

```bash
sudo setcap 'cap_net_bind_service=+ep' /path/to/unpacked/PolarProxy
```
Afterward, we distinct between the two cases **Termination Proxy** and **Reverse Proxy**. The former is used when the server inside the VM is not running with TLS or also accepts unencrypted connections, the latter when the service inside the VM exposes a TLS port.

![Illustration of the setup](images/polarproxy-modes.svg)


To launch PolarProxy in **Termination Proxy** mode, we can use the following command:

```bash
./PolarProxy -p 198.51.100.XX,YY,YY,ZZ -cn "<INSERT TLS CN NAME HERE>" -o /mnt/data/pcaps/ --terminate --connect 192.168.XX.2 --nosni 198.51.100.XX -v 
```

Here, the IP address specified in `-p` and `--nosni` is the external IP address we reserved for the single VM. In case the honeypot is not just reachable by the IP address, but under a domain or other DNS name, `--nosni` should be the domain name or DNS name.

The ports in `-p` define in the given order that:

* We want to listen on port YY
* Decrypted traffic should be stored as port YY in the PCAP
* We want to connect to port ZZ on the specified IP address in `-connect`

 `--connect` holds the internal IP address and `--terminate` defines that we want to terminate connect to the specified. The `-cn` argument defines the Common Name PolarProxy should use for the dynamically generated TLS certificate. While it is optional to use, it makes sense to define a manual one for a honeypot, given that we do not want to advertise to the outside world that PolarProxy is running on this port. Alternatively, a static server certificate can be used with the `--servercert` option.

For **Reverse Proxy** mode, we essentially only need to remove the `--terminate` option and adjust the target port for the `-p` argument. 

However, in the case of a honeypot, it often makes sense to use the same certificate as the underlying service that is running TLS. Given that PolarProxy expects the more unusual `.p12` format that contains both the certificate and the private key in one file, we likely first need to obtain the certificate and private key from inside the VM, and convert them with the following command:

```bash
openssl pkcs12 -export -out cert.p12 -in cert.pem -inkey key.pem
```

OpenSSL will prompt for a password, for which we can just use a value such as `12345` or a more complex value, if desired.


With these adjustments, we can launch PolarProxy in Reverse Proxy mode with a fixed server certificate, using the same certificate and key as the service inside the VM:
```bash
./PolarProxy -p 198.51.100.XX,YY,YY,YY -o /mnt/data/pcaps/ --connect 192.168.XX.2 --nosni 192.168.XX.2 -v --servercert 198.51.100.XX,192.168.XX.2:/path/to/cert.p12:12345
```

Again, if the honeypot is reachable under a domain or another DNS name, `--nosni` needs to hold the domain or DNS name, and the same name should be appended to the `--servercert` argument which also holds the list of domains the specified TLS certificate should be used for.

When running **PolarProxy in combination with TShark**, it can make sense to exclude the TLS port from the TShark capture to avoid bloated PCAP files containing redunant encrypted traffic. This can be achieved with a capture filter in TShark:

```bash
tshark -i vlan.XX -w /mnt/data/pcaps/vlanXX.pcap -f "not ((src net 192.168.XX.1) and (dst net 192.168.XX.2 and dst port YZ)) or ((src net 192.168.XX.2 and src port YZ) and (dst net 192.168.XX.1))"
```
Here, YZ is the last port defined in `-p` for PolarProxy, which is the port from the VM PolarProxy connects to. For the examples above, it is ZZ for the termination mode and YY for the reverse proxy mode.

## Suricata (IDS)
In order to be alerted of incoming attacks, it makes sense to install an IDS that monitors the network traffic for known attacks. For this case, we use [Suricata](https://suricata.readthedocs.io/en/latest/install.html#binary-packages), which can also monitor TLS traffic when combined with PolarProxy.

### Installation
For the installation, we refer to the [binary package installation guide](https://suricata.readthedocs.io/en/latest/install.html#binary-packages) in the official documentation. For a broader level of attack detection, it might make sense to enable additional sources for rules.

The list of default sources for rules can be queried with the first command, and single sources can be enabled with the second command:
```bash
suricata-update list-sources # Query the list of available sources
suricata-update enable-source <source-name> # Enable a specific source
```

### Adding dummy network interfaces for TLS traffic
*(This step can be skipped if we do not want to monitor TLS traffic with Suricata)*

Suppose we want to pipe the decrypted TLS traffic from PolarProxy to Suricata. In that case, we need to create one or multiple dummy network interfaces which Suricata can listen on next to the internet-connected network interface. Unfortunately, netplan does not support the creation of  (persistent) dummy network interfaces. Therefore, we manually create a dummy network interface which is not persistent across reboots:

```bash
sudo ip link add polarproxytls type dummy
```

### Configuration
While the specific detection settings are different for each use case, the main changes we need to perform to the Suricata configuration are to adjust the `HOME_NET`, and to add any dummy network interfaces for use with PolarProxy.

For `HOME_NET`, it makes sense to add the external IP address for a complete monitoring of the whole honeypot network:
```yaml
HOME_NET: "[192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,198.51.100.XX/24]"
```

Then, for the network interfaces, we specifically defined only the internet-connected facing network interface to avoid capturing all possible VLAN interfaces with duplicate and redundant traffic, and the dummy interface created for PolarProxy:

```yaml
af-packet:
  - interface: enp4s0f0
    cluster-id: 1
    cluster-type: cluster_flow
    defrag: yes
    buffer-size: 131072
    
  - interface: polarproxytls
    cluster-id: 2
    cluster-type: cluster_flow
    defrag: yes
```

Further adjustments can be made for other detection related settings. 

To start Suricata and let it autostart upon reboot, we can use:
```bash
sudo systemctl enable filebeat
sudo systemctl start filebeat
```

### Pipe TLS traffic to the dummy network interface
To pipe any traffic from PolarProxy to the dummy network interface Suricata listens on, we use PolarProxy's PCAP-over-IP capabilities combined with `tcpreplay`.

First, we need to allow loopback traffic so that `tcpreplay` can connect to any PCAP-over-IP ports from PolarProxy. 

We can either create a blanket rule that allows unrestricted flow of loopback traffic:
```bash
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
```

Alternatively, a specific rule to only allow a single port can also be used, with 4430 being a replaceable example port we use for PCAP-over-IP.

```bash
sudo iptables -A INPUT -i lo -p tcp --dport 4430 -j ACCEPT
```

Then, we can append `--pcapoverip 4430` to the PolarProxy arguments, start PolarProxy and in another terminal session, launch `tcpreplay`:
```bash
nc localhost 4430 | sudo tcpreplay -i polarproxytls -t -
```

More details and information on how to make this setup persistent can be found in a [blog post from NETRESEC](https://www.netresec.com/?page=Blog&month=2020-01&post=Sniffing-Decrypted-TLS-Traffic-with-Security-Onion).

## ELK (Gateway Machine)
The Elastic toolset provides a wide variety of valuable tools for SIEM. In our use case, we can use it to store and analyze the networking data from the Gateway Server but also collect events from inside the VMs themselves, such as executed commands or other suspicious activities detected by [Falco](https://falco.org/). 

Unfortunately, given that the setup from the master's thesis was based on Elasticsearch 7, with Elasticsearch 8 having made many changes concerning TLS, the same configuration does not make sense to use in the same way as before anymore. Therefore, this section provides a relatively high-level view of how to combine each tool, with the details being omitted.


### ElasticSearch (Installation in Docker)
We assume that ElasticSearch are installed inside a Docker container on the Gateway Machine. An example of setting ElasticSearch and Kibana up together can be [the docker-compose example](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file) listed in the documentation for ElasticSearch. While it seems wasteful to have a multi-node setup running on the same host machine in terms of resources, it can lead to funky behavior later down the road when modifying the `docker-compose.yml` file to only run as a single node.

To harden the ElasticSearch setup and break any isolation between the different VMs, we disallow it to create any new outgoing connections to the VMs. Only connections initiated by the VMs should be accepted:
```bash
sudo iptables -I DOCKER-USER -s 172.16.0.0/12 -m state --state NEW -m iprange --dst-range 192.168.0.0-192.168.255.255 -j DROP
```

In addition, we again only want to allow a specific trusted subnet to be able to access both Elasticsearch and Kibana from outside the machine, with all other connections being dropped:

```bash
sudo iptables -I DOCKER-USER -i enp4s0f0 -p tcp -m conntrack --ctorigdstport 5601 ! -s 192.0.2.0/24 -j DROP
sudo iptables -I DOCKER-USER -i enp4s0f0 -p tcp -m conntrack --ctorigdstport 9200 ! -s 192.0.2.0/24 -j DROP
```

Same as before, replace `192.0.2.0/24` with your trusted subnet or IP.

### Filebeat & Packetbeat
On the Gateway Server, we install Filebeat to collect the Suricata events, and Packetbeat to create visualizations for the network traffic.

Both services are installed outside of Docker, using the `.deb` releases using the official installation tutorial [for Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html#installation) and [for Packetbeat](https://www.elastic.co/guide/en/beats/packetbeat/current/packetbeat-installation-configuration.html#installation). Note that while using APT is also possible, unexpected upgrades can break parts of the installation, either when using inconsistent versions, or when using API keys with tight permissions (as we do later).

Both links also provide general short instructions on how to connect both Beats to Elasticserach. For the Gateway Server, we can use `localhost:9200` as the address. However, in case you did not set up the loopback firewall rules before, you either need to add the blanket "allow all loopback" traffic rule from before, or add the following specific exemptions:

```bash
sudo iptables -A INPUT -i lo -p tcp --dport 5601 -j ACCEPT
sudo iptables -A INPUT -i lo -p tcp --dport 9200 -j ACCEPT
```

For both tools, as stated in each installation tutorial, it makes sense to configure `setup.kibana` section in the config to automatically create dashboards in Kibana. In the setup from the thesis, two Kibana spaces in combination with the optional `space.id` parameter were used to distinct between the data from the Gateway Machine, and the data from the VMs.

For **Filebeat**, we enable the optional Suricata module to collect data from the Suricata EVE logs. This option needs to be enabled in Suricata, which it is by default.

First, we enable the module:
```bash
sudo filebeat modules enable suricata
``` 

Then, we can specify the path for the file in `/etc/filebeat/modules/suricata.yml`. In our case, this matches the default configuration:

```yml
- module: suricata
  eve:
    enabled: true
    var.paths: ["/var/log/suricata/eve.json"]
```


Afterward, we can call eventuelly start Filebeat:
```bash
sudo filebeat setup
sudo systemctl enable filebeat
sudo systemctl start filebeat
```

For **Packetbeat**, after the general connection setup to Elasticsearch and Kibana, we add or modify the following entries in the configuration:

```yaml
# Only listen on the internet-connected interface, similar to Suricata
packetbeat.interfaces.device: enp4s0f0

# Enable af_packet with a slightly increased ring buffer size
packetbeat.interfaces.type: af_packet
packetbeat.interfaces.buffer_size_mb: 150

# Enable GeoIP enrichment
output.elasticsearch.pipeline: geoip-info
```

Unfortunately, we cannot define multiple network interfaces in Packetbeat similar as in Suricata without restorting to the `any` interface, which captures *all* network devices including the VLANs. Therefore, we limit ourselves here to the internet-connected network interface.

Now, we can start Packetbeat in the same fashion as Filebeat:
```bash
sudo filebeat setup
sudo systemctl enable filebeat
sudo systemctl start filebeat
```

After the initial launch, if you did not already do it before, we can downgrade the credentials to the least possible privilege by creating an API key with minimal permissions for adding new entries. While this is not strictly necessary for the Gateway Machine, given that it is part of the "Trusted" infrastructure, it might still prevent some harm. Examples on how to create such an API key can be found in the official documentation for [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/beats-api-keys.html#beats-api-key-publish) and for [Packetbeat](https://www.elastic.co/guide/en/beats/filebeat/current/beats-api-keys.html#beats-api-key-publish).

### Logstash (Gateway Server, Slack Alerts)
In addition to the Beats, Logstash can be used on the same Suricata EVE log to send alerts to a Slack channel when high-severity attacks were detected.

To replicate this, [install Logstash](https://www.elastic.co/downloads/logstash) and the 3rd-party [Slack Output Plugin](https://github.com/logstash-plugins/logstash-output-slack). Then, a Logstash configuration needs to be added. An example which automatically sends Suricata alerts with "Level 1" severity can be found [here](logstash-suricata.conf), though from personal experience, it can be quite noisy and therefore might need further adjustments. The configuration file(s) need to be copied to `/etc/logstash/conf.d`, and afterward, Logstash can be started:

```bash
sudo systemctl enable logstash
sudo systemctl start logstash
```


## ELK & Falco (VMs)
After describing the setup on the Gateway Machine in the previous section, we now switch to the configuration inside the VM that allows us to track the behavior of attackers and additional generic metrics data. Note that this setup is not 100% ideal, given that everything runs as user-space processes which attackers can potentially kill or steal the credentials for. However, due to a lack of commonly available kernel-level surveillance modules for recent kernel versions, we use a common SIEM-based approach with tight permissions that should prevent the abuse of the Elasticsearch server.

### Falco
Before we set up the Beats, we first install Falco using the official [installation guide](https://falco.org/docs/getting-started/installation/#installing). While Falco is primarily focused on container-based attacks, it nevertheless contains useful rules for other kinds of attacks and suspicious activities. 

Before we start Falco, we need to enable the file output in the configuration in order for Filebeat to be able to collect any data for Falco. This can be achieved by creating the necessary directory:

```bash
sudo mkdir /var/log/falco
```

And adding the following entry to `/etc/falco/falco.yaml`
```yaml
file_output:
  enabled: true
  keep_alive: false
  filename: /var/log/falco/falco.json
```

Afterwards, Falco can be started:
```bash
sudo systemctl enable falco
sudo systemctl start falco
```

### Auditbeat, Filebeat, Metricbeat
Similar as for the Gateway machine, [Auditbeat](https://www.elastic.co/guide/en/beats/auditbeat/current/auditbeat-installation-configuration.html#install), [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html) and [Metricbeat](https://www.elastic.co/guide/en/beats/metricbeat/current/metricbeat-installation-configuration.html) can be installed and configured following the official installation tutorial.

For the Elasticsearch server IP address, we need to use the internal IP address of the Gateway Server for `output.elasticsearch.hosts`:
```yaml
output.elasticsearch:
  hosts: ["192.168.XX.1:9200"]
```

In addition, on the Gateway Server, we need to add an additional rule to allow a VM to make a connection to Elasticsearch:
```bash
sudo iptables -I DOCKER-USER -s 192.168.XX.2 -d 172.16.0.0/12 -p tcp --dport 9200 -m state --state NEW -j ACCEPT
```

Given that the VMs run in an untrusted environment, the use of API keys is of very importance to prevent potential attackers from compromising the Elasticsearch server. However, on the very first use of the tools, the necessary indices are not created yet in Elasticsearch. The same applies to the Kibana dashboards, especially when running under a different `space.id`. Therefore, it either makes sense to run this setup in one trusted VM first with admin credentials (which should be securely wiped after the initial setup), or adapt the API key permissions to allow the creation of indicies and other required options. Following the principle of least privilege, the first option is preferable with an ephemeral trusted VM that is created to validate the setup and destroyed afterwards without any exposure to attackers.

But before we initally run each Beat, we make the following changes to the configuration:

1. For **Auditbeat**, we need to add audit rules which Auditbeat should pass to the Linux kernel. For the setup in the thesis, a slightly modified ruleset from [Florian Roth's Auditd rules](https://github.com/Neo23x0/auditd), with incompatible rules for Auditbeat and Ubuntu 20.04 being removed. The used rules can be found as part of this repository in [audit-rules.conf](audit-rules.conf), though the rules might not be ideal for every use case and outdated after time of this writing.

2. To integrate Falco with **Filebeat**, we need to add the following input to `/etc/filebeat/filebeat.yml`:
```yaml
filebeat.inputs:
- type: filestream
  enabled: true
  paths:
    - /var/log/falco/falco.json
  parsers:
    - ndjson:
      keys_under_root: true
      add_error_key: true
  index: "falco-%{+yyyy.MM.dd}"
  ```

With all configurations into place, we can finally do an initial run for each tool using admin credentials or privileged API keys from a trusted VM.

After the initial run, we can create API keys with the least required permissions to be used inside the honeypot VMs. We can use the official documentation to create the API keys for [Auditbeat](https://www.elastic.co/guide/en/beats/auditbeat/master/beats-api-keys.html#beats-api-key-publish) and [Metricbeat] (https://www.elastic.co/guide/en/beats/metricbeat/current/beats-api-keys.html#beats-api-key-publish).

For Filebeat, due to the additional Falco index, we need to slightly adapt the API key example from the documentation:

```json
POST /_security/api_key
{
  "name": "filebeat_hostXXX", 
  "role_descriptors": {
    "filebeat_writer": { 
      "cluster": ["monitor", "read_ilm", "read_pipeline"],
      "index": [
        {
          "names": ["filebeat-*"],
          "privileges": ["view_index_metadata", "create_doc"]
        },
        {
          "names": ["falco-*"],
          "privileges": ["view_index_metadata", "create_doc"]
        }
      ]
    }
  }
}
```

### Filtering Beats traffic from the PCAPs
When the Beats inside the VM communicate with the ElasticSearch server on the Gateway Server, the traffic is passed through the same network interface we are capturing. Since the Beats, especially Metricbeat, can produce quite a lot of data bloating up the PCAPs, we might not want to include it in the packet capture data we collect with TShark. 

Using the same suggested filtering approach as above, we can instruct TShark to filter out any data going from or to ElasticSearch:
```bash
tshark -i vlan.XX -w /mnt/data/pcaps/vlanXX.pcap -f "not ((src net 192.168.XX.1 and src port 9200) or (dst net 192.168.XX.1 and dst port 9200))"
```

When already using the TLS or any other capture filter, we append the above capture filter to the existing one with an `and`. As an example with the suggested TLS filter:

```bash
tshark -i vlan.XX -w /mnt/data/pcaps/vlanXX.pcap -f "not ((src net 192.168.XX.1) and (dst net 192.168.XX.2 and dst port YZ)) or ((src net 192.168.XX.2 and src port YZ) and (dst net 192.168.XX.1)) and not ((src net 192.168.XX.1 and src port 9200) or (dst net 192.168.XX.1 and dst port 9200))"
```

The letter conventions are the same as the previous examples in the packet capturing section, with XX being the VLAN ID and YZ the port from the VM PolarProxy connects to in either termination proxy mode (ZZ) or reverse proxy mode (YY).


> **Deep fetch: 1 key files fetched beyond README.**



---

# FILE: netplan.yaml

# This is the network config written by 'subiquity'
network:
  version: 2
  ethernets:
    enp4s0f0:
      addresses: 
        - 198.51.100.42/24 # Gateway server external IP address 
        - 198.51.100.4/24 # Honeypot Service
        - 198.51.100.12/24 # Another Honeypot Service
      gateway4: 198.51.100.1
      dhcp4: false
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
    enp7s0f0:
      dhcp4: false
      addresses: [192.168.1.1/30]
  vlans:
    vlan.2:
      id: 2
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.2.1/30]
    vlan.3:
      id: 3
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.3.1/30]
    vlan.4:
      id: 4
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.4.1/30]
    vlan.5:
      id: 5
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.5.1/30]
    vlan.6:
      id: 6
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.6.1/30]
    vlan.7:
      id: 7
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.7.1/30]
    vlan.8:
      id: 8
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.8.1/30]
    vlan.9:
      id: 9
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.9.1/30]
    vlan.10:
      id: 10
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.10.1/30]
    vlan.11:
      id: 11
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.11.1/30]
    vlan.12:
      id: 12
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.12.1/30]
    vlan.13:
      id: 13
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.13.1/30]
    vlan.14:
      id: 14
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.14.1/30]
    vlan.15:
      id: 15
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.15.1/30]
    vlan.16:
      id: 16
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.16.1/30]
    vlan.17:
      id: 17
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.17.1/30]
    vlan.18:
      id: 18
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.18.1/30]
    vlan.19:
      id: 19
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.19.1/30]
    vlan.20:
      id: 20
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.20.1/30]
    vlan.21:
      id: 21
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.21.1/30]
    vlan.22:
      id: 22
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.22.1/30]
    vlan.23:
      id: 23
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.23.1/30]
    vlan.24:
      id: 24
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.24.1/30]
    vlan.25:
      id: 25
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.25.1/30]
    vlan.26:
      id: 26
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.26.1/30]
    vlan.27:
      id: 27
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.27.1/30]
    vlan.28:
      id: 28
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.28.1/30]
    vlan.29:
      id: 29
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.29.1/30]
    vlan.30:
      id: 30
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.30.1/30]
    vlan.31:
      id: 31
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.31.1/30]
    vlan.32:
      id: 32
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.32.1/30]
    vlan.33:
      id: 33
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.33.1/30]
    vlan.34:
      id: 34
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.34.1/30]
    vlan.35:
      id: 35
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.35.1/30]
    vlan.36:
      id: 36
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.36.1/30]
    vlan.37:
      id: 37
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.37.1/30]
    vlan.38:
      id: 38
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.38.1/30]
    vlan.39:
      id: 39
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.39.1/30]
    vlan.40:
      id: 40
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.40.1/30]
    vlan.41:
      id: 41
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.41.1/30]
    vlan.42:
      id: 42
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.42.1/30]
    vlan.43:
      id: 43
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.43.1/30]
    vlan.44:
      id: 44
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.44.1/30]
    vlan.45:
      id: 45
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.45.1/30]
    vlan.46:
      id: 46
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.46.1/30]
    vlan.47:
      id: 47
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.47.1/30]
    vlan.48:
      id: 48
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.48.1/30]
    vlan.49:
      id: 49
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.49.1/30]
    vlan.50:
      id: 50
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.50.1/30]
    vlan.51:
      id: 51
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.51.1/30]
    vlan.52:
      id: 52
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.52.1/30]
    vlan.53:
      id: 53
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.53.1/30]
    vlan.54:
      id: 54
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.54.1/30]
    vlan.55:
      id: 55
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.55.1/30]
    vlan.56:
      id: 56
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.56.1/30]
    vlan.57:
      id: 57
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.57.1/30]
    vlan.58:
      id: 58
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.58.1/30]
    vlan.59:
      id: 59
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.59.1/30]
    vlan.60:
      id: 60
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.60.1/30]
    vlan.61:
      id: 61
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.61.1/30]
    vlan.62:
      id: 62
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.62.1/30]
    vlan.63:
      id: 63
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.63.1/30]
    vlan.64:
      id: 64
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.64.1/30]
    vlan.65:
      id: 65
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.65.1/30]
    vlan.66:
      id: 66
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.66.1/30]
    vlan.67:
      id: 67
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.67.1/30]
    vlan.68:
      id: 68
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.68.1/30]
    vlan.69:
      id: 69
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.69.1/30]
    vlan.70:
      id: 70
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.70.1/30]
    vlan.71:
      id: 71
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.71.1/30]
    vlan.72:
      id: 72
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.72.1/30]
    vlan.73:
      id: 73
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.73.1/30]
    vlan.74:
      id: 74
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.74.1/30]
    vlan.75:
      id: 75
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.75.1/30]
    vlan.76:
      id: 76
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.76.1/30]
    vlan.77:
      id: 77
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.77.1/30]
    vlan.78:
      id: 78
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.78.1/30]
    vlan.79:
      id: 79
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.79.1/30]
    vlan.80:
      id: 80
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.80.1/30]
    vlan.81:
      id: 81
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.81.1/30]
    vlan.82:
      id: 82
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.82.1/30]
    vlan.83:
      id: 83
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.83.1/30]
    vlan.84:
      id: 84
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.84.1/30]
    vlan.85:
      id: 85
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.85.1/30]
    vlan.86:
      id: 86
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.86.1/30]
    vlan.87:
      id: 87
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.87.1/30]
    vlan.88:
      id: 88
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.88.1/30]
    vlan.89:
      id: 89
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.89.1/30]
    vlan.90:
      id: 90
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.90.1/30]
    vlan.91:
      id: 91
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.91.1/30]
    vlan.92:
      id: 92
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.92.1/30]
    vlan.93:
      id: 93
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.93.1/30]
    vlan.94:
      id: 94
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.94.1/30]
    vlan.95:
      id: 95
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.95.1/30]
    vlan.96:
      id: 96
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.96.1/30]
    vlan.97:
      id: 97
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.97.1/30]
    vlan.98:
      id: 98
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.98.1/30]
    vlan.99:
      id: 99
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.99.1/30]
    vlan.100:
      id: 100
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.100.1/30]
    vlan.101:
      id: 101
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.101.1/30]
    vlan.102:
      id: 102
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.102.1/30]
    vlan.103:
      id: 103
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.103.1/30]
    vlan.104:
      id: 104
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.104.1/30]
    vlan.105:
      id: 105
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.105.1/30]
    vlan.106:
      id: 106
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.106.1/30]
    vlan.107:
      id: 107
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.107.1/30]
    vlan.108:
      id: 108
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.108.1/30]
    vlan.109:
      id: 109
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.109.1/30]
    vlan.110:
      id: 110
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.110.1/30]
    vlan.111:
      id: 111
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.111.1/30]
    vlan.112:
      id: 112
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.112.1/30]
    vlan.113:
      id: 113
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.113.1/30]
    vlan.114:
      id: 114
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.114.1/30]
    vlan.115:
      id: 115
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.115.1/30]
    vlan.116:
      id: 116
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.116.1/30]
    vlan.117:
      id: 117
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.117.1/30]
    vlan.118:
      id: 118
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.118.1/30]
    vlan.119:
      id: 119
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.119.1/30]
    vlan.120:
      id: 120
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.120.1/30]
    vlan.121:
      id: 121
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.121.1/30]
    vlan.122:
      id: 122
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.122.1/30]
    vlan.123:
      id: 123
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.123.1/30]
    vlan.124:
      id: 124
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.124.1/30]
    vlan.125:
      id: 125
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.125.1/30]
    vlan.126:
      id: 126
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.126.1/30]
    vlan.127:
      id: 127
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.127.1/30]
    vlan.128:
      id: 128
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.128.1/30]
    vlan.129:
      id: 129
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.129.1/30]
    vlan.130:
      id: 130
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.130.1/30]
    vlan.131:
      id: 131
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.131.1/30]
    vlan.132:
      id: 132
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.132.1/30]
    vlan.133:
      id: 133
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.133.1/30]
    vlan.134:
      id: 134
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.134.1/30]
    vlan.135:
      id: 135
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.135.1/30]
    vlan.136:
      id: 136
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.136.1/30]
    vlan.137:
      id: 137
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.137.1/30]
    vlan.138:
      id: 138
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.138.1/30]
    vlan.139:
      id: 139
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.139.1/30]
    vlan.140:
      id: 140
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.140.1/30]
    vlan.141:
      id: 141
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.141.1/30]
    vlan.142:
      id: 142
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.142.1/30]
    vlan.143:
      id: 143
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.143.1/30]
    vlan.144:
      id: 144
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.144.1/30]
    vlan.145:
      id: 145
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.145.1/30]
    vlan.146:
      id: 146
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.146.1/30]
    vlan.147:
      id: 147
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.147.1/30]
    vlan.148:
      id: 148
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.148.1/30]
    vlan.149:
      id: 149
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.149.1/30]
    vlan.150:
      id: 150
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.150.1/30]
    vlan.151:
      id: 151
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.151.1/30]
    vlan.152:
      id: 152
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.152.1/30]
    vlan.153:
      id: 153
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.153.1/30]
    vlan.154:
      id: 154
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.154.1/30]
    vlan.155:
      id: 155
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.155.1/30]
    vlan.156:
      id: 156
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.156.1/30]
    vlan.157:
      id: 157
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.157.1/30]
    vlan.158:
      id: 158
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.158.1/30]
    vlan.159:
      id: 159
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.159.1/30]
    vlan.160:
      id: 160
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.160.1/30]
    vlan.161:
      id: 161
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.161.1/30]
    vlan.162:
      id: 162
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.162.1/30]
    vlan.163:
      id: 163
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.163.1/30]
    vlan.164:
      id: 164
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.164.1/30]
    vlan.165:
      id: 165
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.165.1/30]
    vlan.166:
      id: 166
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.166.1/30]
    vlan.167:
      id: 167
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.167.1/30]
    vlan.168:
      id: 168
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.168.1/30]
    vlan.169:
      id: 169
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.169.1/30]
    vlan.170:
      id: 170
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.170.1/30]
    vlan.171:
      id: 171
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.171.1/30]
    vlan.172:
      id: 172
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.172.1/30]
    vlan.173:
      id: 173
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.173.1/30]
    vlan.174:
      id: 174
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.174.1/30]
    vlan.175:
      id: 175
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.175.1/30]
    vlan.176:
      id: 176
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.176.1/30]
    vlan.177:
      id: 177
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.177.1/30]
    vlan.178:
      id: 178
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.178.1/30]
    vlan.179:
      id: 179
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.179.1/30]
    vlan.180:
      id: 180
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.180.1/30]
    vlan.181:
      id: 181
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.181.1/30]
    vlan.182:
      id: 182
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.182.1/30]
    vlan.183:
      id: 183
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.183.1/30]
    vlan.184:
      id: 184
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.184.1/30]
    vlan.185:
      id: 185
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.185.1/30]
    vlan.186:
      id: 186
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.186.1/30]
    vlan.187:
      id: 187
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.187.1/30]
    vlan.188:
      id: 188
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.188.1/30]
    vlan.189:
      id: 189
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.189.1/30]
    vlan.190:
      id: 190
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.190.1/30]
    vlan.191:
      id: 191
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.191.1/30]
    vlan.192:
      id: 192
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.192.1/30]
    vlan.193:
      id: 193
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.193.1/30]
    vlan.194:
      id: 194
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.194.1/30]
    vlan.195:
      id: 195
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.195.1/30]
    vlan.196:
      id: 196
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.196.1/30]
    vlan.197:
      id: 197
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.197.1/30]
    vlan.198:
      id: 198
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.198.1/30]
    vlan.199:
      id: 199
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.199.1/30]
    vlan.200:
      id: 200
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.200.1/30]
    vlan.201:
      id: 201
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.201.1/30]
    vlan.202:
      id: 202
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.202.1/30]
    vlan.203:
      id: 203
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.203.1/30]
    vlan.204:
      id: 204
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.204.1/30]
    vlan.205:
      id: 205
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.205.1/30]
    vlan.206:
      id: 206
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.206.1/30]
    vlan.207:
      id: 207
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.207.1/30]
    vlan.208:
      id: 208
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.208.1/30]
    vlan.209:
      id: 209
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.209.1/30]
    vlan.210:
      id: 210
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.210.1/30]
    vlan.211:
      id: 211
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.211.1/30]
    vlan.212:
      id: 212
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.212.1/30]
    vlan.213:
      id: 213
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.213.1/30]
    vlan.214:
      id: 214
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.214.1/30]
    vlan.215:
      id: 215
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.215.1/30]
    vlan.216:
      id: 216
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.216.1/30]
    vlan.217:
      id: 217
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.217.1/30]
    vlan.218:
      id: 218
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.218.1/30]
    vlan.219:
      id: 219
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.219.1/30]
    vlan.220:
      id: 220
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.220.1/30]
    vlan.221:
      id: 221
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.221.1/30]
    vlan.222:
      id: 222
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.222.1/30]
    vlan.223:
      id: 223
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.223.1/30]
    vlan.224:
      id: 224
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.224.1/30]
    vlan.225:
      id: 225
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.225.1/30]
    vlan.226:
      id: 226
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.226.1/30]
    vlan.227:
      id: 227
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.227.1/30]
    vlan.228:
      id: 228
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.228.1/30]
    vlan.229:
      id: 229
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.229.1/30]
    vlan.230:
      id: 230
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.230.1/30]
    vlan.231:
      id: 231
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.231.1/30]
    vlan.232:
      id: 232
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.232.1/30]
    vlan.233:
      id: 233
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.233.1/30]
    vlan.234:
      id: 234
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.234.1/30]
    vlan.235:
      id: 235
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.235.1/30]
    vlan.236:
      id: 236
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.236.1/30]
    vlan.237:
      id: 237
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.237.1/30]
    vlan.238:
      id: 238
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.238.1/30]
    vlan.239:
      id: 239
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.239.1/30]
    vlan.240:
      id: 240
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.240.1/30]
    vlan.241:
      id: 241
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.241.1/30]
    vlan.242:
      id: 242
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.242.1/30]
    vlan.243:
      id: 243
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.243.1/30]
    vlan.244:
      id: 244
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.244.1/30]
    vlan.245:
      id: 245
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.245.1/30]
    vlan.246:
      id: 246
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.246.1/30]
    vlan.247:
      id: 247
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.247.1/30]
    vlan.248:
      id: 248
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.248.1/30]
    vlan.249:
      id: 249
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.249.1/30]
    vlan.250:
      id: 250
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.250.1/30]
    vlan.251:
      id: 251
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.251.1/30]
    vlan.252:
      id: 252
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.252.1/30]
    vlan.253:
      id: 253
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.253.1/30]
    vlan.254:
      id: 254
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.254.1/30]
    vlan.255:
      id: 255
      dhcp4: false
      link: enp7s0f0
      addresses: [192.168.255.1/30]
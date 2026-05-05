# OISF/suricata

Source: https://github.com/OISF/suricata
Ingested: 2026-05-04
Type: documentation

---

# README

# Suricata

[![Fuzzing Status](https://oss-fuzz-build-logs.storage.googleapis.com/badges/suricata.svg)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:suricata)
[![codecov](https://codecov.io/gh/OISF/suricata/branch/main/graph/badge.svg?token=QRyyn2BSo1)](https://codecov.io/gh/OISF/suricata)

## Introduction

[Suricata](https://suricata.io) is a network IDS, IPS and NSM engine
developed by the [OISF](https://oisf.net) and the Suricata community.

## Resources

- [Home Page](https://suricata.io)
- [Bug Tracker](https://redmine.openinfosecfoundation.org/projects/suricata)
- [User Guide](https://docs.suricata.io)
- [Dev Guide](https://docs.suricata.io/en/latest/devguide/index.html)
- [Installation Guide](https://docs.suricata.io/en/latest/install.html)
- [User Support Forum](https://forum.suricata.io)

## Contributing

We're happily taking patches and other contributions. Please see our
[Contribution
Process](https://docs.suricata.io/en/latest/devguide/contributing/contribution-process.html)
for how to get started.

Suricata is a complex piece of software dealing with mostly untrusted
input. Mishandling this input will have serious consequences:

* in IPS mode a crash may knock a network offline
* in passive mode a compromise of the IDS may lead to loss of critical
  and confidential data
* missed detection may lead to undetected compromise of the network

In other words, we think the stakes are pretty high, especially since
in many common cases the IDS/IPS will be directly reachable by an
attacker.

For this reason, we have developed a QA process that is quite
extensive. A consequence is that contributing to Suricata can be a
somewhat lengthy process.

On a high level, the steps are:

1. GitHub-CI based checks. This runs automatically when a pull request
   is made.
2. Review by devs from the team and community
3. QA runs from private QA setups. These are private due to the nature
   of the test traffic.

### Overview of Suricata's QA steps

OISF team members are able to submit builds to our private QA
setup. It will run a series of build tests and a regression suite to
confirm no existing features break.

The final QA runs takes a few hours minimally, and generally runs
overnight. It currently runs:

- extensive build tests on different OS', compilers, optimization
  levels, configure features
- static code analysis using cppcheck, scan-build
- runtime code analysis using valgrind, AddressSanitizer,
  LeakSanitizer
- regression tests for past bugs
- output validation of logging
- unix socket testing
- pcap based fuzz testing using ASAN and LSAN
- traffic replay based IDS and IPS tests

Next to these tests, based on the type of code change further tests
can be run manually:

- traffic replay testing (multi-gigabit)
- large pcap collection processing (multi-terabytes)
- fuzz testing (might take multiple days or even weeks)
- pcap based performance testing
- live performance testing
- various other manual tests based on evaluation of the proposed
  changes

It's important to realize that almost all of the tests above are used
as acceptance tests. If something fails, it's up to you to address
this in your code.

One step of the QA is currently run post-merge. We submit builds to
the Coverity Scan program. Due to limitations of this (free) service,
we can submit once a day max.  Of course it can happen that after the
merge the community will find issues. For both cases we request you to
help address the issues as they may come up.

## FAQ

__Q: Will you accept my PR?__

A: That depends on a number of things, including the code
quality. With new features it also depends on whether the team and/or
the community think the feature is useful, how much it affects other
code and features, the risk of performance regressions, etc.

__Q: When will my PR be merged?__

A: It depends, if it's a major feature or considered a high risk
change, it will probably go into the next major version.

__Q: Why was my PR closed?__

A: As documented in the [Suricata GitHub
workflow](https://docs.suricata.io/en/latest/devguide/contributing/github-pr-workflow.html),
we expect a new pull request for every change.

Normally, the team (or community) will give feedback on a pull request
after which it is expected to be replaced by an improved PR. So look
at the comments. If you disagree with the comments we can still
discuss them in the closed PR.

If the PR was closed without comments it's likely due to QA
failure. If the GitHub-CI checks failed, the PR should be fixed right
away. No need for a discussion about it, unless you believe the QA
failure is incorrect.

__Q: The compiler/code analyser/tool is wrong, what now?__

A: To assist in the automation of the QA, we're not accepting warnings
or errors to stay. In some cases this could mean that we add a
suppression if the tool supports that (e.g. valgrind, DrMemory). Some
warnings can be disabled. In some exceptional cases the only
'solution' is to refactor the code to work around a static code
checker limitation false positive. While frustrating, we prefer this
over leaving warnings in the output. Warnings tend to get ignored and
then increase risk of hiding other warnings.

__Q: I think your QA test is wrong__

A: If you really think it is, we can discuss how to improve it. But
don't come to this conclusion too quickly, more often it's the code
that turns out to be wrong.

__Q: Do you require signing of a contributor license agreement?__

A: Yes, we do this to keep the ownership of Suricata in one hand: the
Open Information Security Foundation. See
http://suricata.io/about/open-source/ and
http://suricata.io/about/contribution-agreement/



> **Deep fetch: 6 key files fetched beyond README.**



---

# FILE: .readthedocs.yaml

# Required by Read The Docs
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

python:
  install:
    - requirements: doc/userguide/requirements.txt

sphinx:
  builder: html
  configuration: doc/userguide/conf.py
  fail_on_warning: false

formats: all



---

# FILE: SECURITY.md

# Security Policy

Being a security tool itself, the security of Suricata itself is naturally of
great importance. This document describes the policy around security issues as
well as how to report them.

If you believe you found a vulnerability, please report it to us as described
in this document.


## Severity Levels

We will determine the severity of each issue, taking into account our
experience dealing with past issues, versions affected, common defaults,
our estimate of exploitation complexity, part of the code affected,
and use cases. We use the following severity categories:

* **CRITICAL** Severity. This affects Tier 1 features that are enabled by default
where the issue disrupts availability of the service, leading to severe
loss of visibility and/or availability. Remotely triggerable traffic
based code execution, crashes, or evasions with a wide scope are considered to be
in-scope for this severity. These issues will be kept private and will trigger a
new release of all supported versions. We will attempt to address these as soon
as possible.

* **HIGH** Severity. This includes issues that are of a lower risk than critical,
perhaps due to being disabled by default Tier 1 or affecting Tier 2 and
Community features, or which are less likely to be exploitable. These issues
will be kept private and will trigger a new release of all supported versions.
We will attempt to keep the time these issues are private to a minimum; our
aim would be no longer than a month where this is something under our control.

* **MODERATE** Severity. This includes issues like crashes or evasion in Tier 2 and
Community features that are not enabled by default. These will in general be
kept private until the next release, and that release will be scheduled so
that it can roll up several such flaws at one time.

* **LOW** Severity. This includes issues such as those that only affect the
Suricata command line utilities, or unlikely configurations. These will in
general be fixed as soon as possible in latest development versions, and may be
backported to older versions that are still getting updates. These will be
part of the Changelog as a security ticket, but they may not trigger new
releases.

Note that we'll be refining the levels based on our experiences with applying them
to actual issues.

## CVE ID's and Github Security Advisories (GHSA)

We will request a CVE ID for an issue if appropriate. Note that multiple
issues may share the same CVE ID.

We work with the Github CNA, through the Github Security Advisory (GHSA) facility.

The GHSA's will be published at least 2 weeks after the public release addressing
the issue, together with the redmine security tickets.

## Support Status of affected code

4 levels are defined: Tier 1, Tier 2, Community and Unmaintained.

These are documented in https://docs.suricata.io/en/latest/support-status.html


## Reporting Issues

For reporting security issues, please use `security@oisf.net`.

If you report a security issue to us, please share as much detail about the issue
as possible: pcaps, attack scripts, potential fixes, etc. If you share pcaps or
other data, please clearly state if these can (eventually) enter our public CI/QA.

We will assign a severity and will share our assessment with you.

We will create a security ticket, which will be private until at least 2 weeks after
a public release addressing the issue.

We will acknowledge you in the release notes, release announcement and GHSA. If you
do not want this, please clearly state this. For the GHSA credits, please give us
your github handle.

Please let us know if you've requested a CVE ID. If you haven't, we can do it.

OISF does not participate in bug bounty programs, or offer any other rewards
for reporting issues.



---

# FILE: examples/lib/custom/README.md

# Custom Library Example

This is an example of using the Suriata library with your own packets
and threads.

## Building In Tree

The Suricata build system has created a Makefile that should allow you
to build this application in-tree on most supported platforms. To
build simply run:

```
make
```

## Running

```
./custom -l . -- filename.pcap
```

For this example, any arguments before `--` are passed directly as
Suricata command line arguments. Arguments after the first `--` are
handled by this example program, and currently the only argument is a
PCAP filename to be read.

## Building Out of Tree

A Makefile.example has also been generated to use as an example on how
to build against the library in a standalone application.

First build and install the Suricata library including:

```
make install-library
make install-headers
```

Then run:

```
make -f Makefile.example
```

If you installed to a non-standard location, you need to ensure that
`libsuricata-config` is in your path, for example:

```
PATH=/opt/suricata/bin:$PATH make -f Makefile.example
```



---

# FILE: examples/lib/live/README.md

# Live Capture Library Example

This is an example of using the Suricata library to capture live
traffic from a network interface with custom packet handling and
threading.

## Building In Tree

The Suricata build system has created a Makefile that should allow you
to build this application in-tree on most supported platforms. To
build simply run:

```
make
```

## Running

```
./live -i eth0 -l .
```

This example requires at least one `-i` option to specify the network
interface to capture from. You can specify multiple interfaces to
capture from multiple sources simultaneously - a separate worker thread
will be created for each interface:

```
./live -i eth0 -i eth1
```

Any additional arguments are passed directly to Suricata as command
line arguments.

Example with common options:
```
sudo ./live -i eth0 -- -l . -S rules.rules
```

Example capturing from multiple interfaces:
```
sudo ./live -i eth0 -i wlan0 -- -l . -S rules.rules
```

Shutdown: each worker thread may call EngineStop when its capture ends; the
main loop waits for this signal, performs SuricataShutdown concurrently with
per-thread SCTmThreadsSlotPacketLoopFinish, then joins all worker threads
before GlobalsDestroy.

The example supports up to 16 interfaces simultaneously.

## Building Out of Tree

A Makefile.example has also been generated to use as an example on how
to build against the library in a standalone application.

First build and install the Suricata library including:

```
make install-library
make install-headers
```

Then run:

```
make -f Makefile.example
```

If you installed to a non-standard location, you need to ensure that
`libsuricata-config` is in your path, for example:

```
PATH=/opt/suricata/bin:$PATH make -f Makefile.example
```



---

# FILE: examples/lib/simple/README.md

# Simple Library Example

## Building In Tree

The Suricata build system has created a Makefile that should allow you
to build this application in-tree on most supported platforms. To
build simply run:

```
make
```

## Building Out of Tree

A Makefile.example has also been generated to use as an example on how
to build against the library in a standalone application.

First build and install the Suricata library including:

```
make install-library
make install-headers
```

Then run:

```
make -f Makefile.example
```

If you installed to a non-standard location, you need to ensure that
`libsuricata-config` is in your path, for example:

```
PATH=/opt/suricata/bin:$PATH make -f Makefile.example
```



---

# FILE: rules/README.md

# Suricata Reserved SID Allocations

Unless otherwise noted, each component or protocol is allocated 1000
signature IDs.

## Components

| Component         | Start   | End     |
| ----------------- | ------- | ------- |
| Decoder           | 2200000 | 2200999 |
| Stream            | 2210000 | 2210999 |
| Generic App-Layer | 2260000 | 2260999 |

## App-Layer Protocols

| Protocol | Start   | End     |
| -------- | ------- | ------- |
| SMTP     | 2220000 | 2220999 |
| HTTP     | 2221000 | 2221999 |
| NTP      | 2222000 | 2222999 |
| NFS      | 2223000 | 2223999 |
| IPsec    | 2224000 | 2224999 |
| SMB      | 2225000 | 2225999 |
| Kerberos | 2226000 | 2226999 |
| DHCP     | 2227000 | 2227999 |
| SSH      | 2228000 | 2228999 |
| MQTT     | 2229000 | 2229999 |
| TLS      | 2230000 | 2230999 |
| QUIC     | 2231000 | 2231999 |
| FTP      | 2232000 | 2232999 |
| POP3     | 2236000 | 2236999 |
| LDAP     | 2237000 | 2237999 |
| DNS      | 2240000 | 2240999 |
| PGSQL    | 2241000 | 2241999 |
| mDNS     | 2242000 | 2242999 |
| MODBUS   | 2250000 | 2250999 |
| DNP3     | 2270000 | 2270999 |
| HTTP2    | 2290000 | 2290999 |

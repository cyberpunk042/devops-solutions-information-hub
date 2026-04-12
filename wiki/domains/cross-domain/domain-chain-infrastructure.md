---
title: "Artifact Chain: Infrastructure/IaC Domain"
type: reference
domain: cross-domain
status: synthesized
confidence: medium
maturity: seed
created: 2026-04-12
updated: 2026-04-12
sources:
  - id: taxonomy
    type: wiki
    file: wiki/domains/cross-domain/methodology-artifact-taxonomy.md
  - id: terraform-docs
    type: documentation
    url: "https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code"
tags: [methodology, artifact-chain, infrastructure, terraform, iac, domain-specific, devops-control-plane]
---

# Artifact Chain: Infrastructure/IaC Domain

> [!tip] AI Quick Start — Working on Infrastructure as Code
>
> 1. **Gate commands:** `terraform validate` (syntax), `terraform plan` (changes correct), `terraform apply` (staging only)
> 2. **Scaffold:** `variable` and `output` blocks + module interfaces. NO `resource` blocks. NO `data` sources.
> 3. **Implement:** `resource` blocks + module implementations + existing environment configs reference new modules
> 4. **Test:** `terraform plan` shows expected changes (no surprise destroys) + `terraform apply` succeeds in staging
> 5. **Unique to infra:** Deploy stage (optional, production apply), drift detection (use bug-fix model), state management

## Summary

Artifact chain resolution for Infrastructure as Code projects (devops-control-plane, Terraform, Docker, CI/CD). Maps methodology stages to IaC-specific artifacts. The unique characteristic of this domain: the "scaffold" stage defines infrastructure STRUCTURE (variables, outputs, module interfaces), the "implement" stage creates RESOURCES (actual infrastructure), and the "test" stage verifies via `terraform plan` and `terraform apply` against a staging environment. State management and drift detection add artifact types not found in code domains.

## Reference Content

### Toolchain

> [!info] Infrastructure Domain Stack
>
> | Tool | Purpose | Gate Command |
> |------|---------|-------------|
> | Terraform | Infrastructure provisioning | `terraform validate`, `terraform plan`, `terraform apply` |
> | Docker / docker-compose | Container orchestration | `docker build`, `docker-compose up` |
> | Ansible / Shell scripts | Configuration management | `ansible-playbook --check` |
> | CI/CD (GitHub Actions, etc.) | Deployment pipeline | Pipeline passes |
> | Remote state (S3/GCS) | State management | `terraform init` succeeds |

### Feature Development — Infrastructure Chain

> [!abstract] Full Chain — Document through Deployment
>
> | # | Stage | Artifact | File Pattern | Gate |
> |---|-------|----------|-------------|------|
> | 1 | document | Requirements Spec | `wiki/domains/infrastructure/{slug}-requirements.md` | Infrastructure requirements with capacity/availability/security constraints |
> | 2 | document | Current State Analysis | `wiki/domains/infrastructure/{slug}-current-state.md` | Existing resources mapped with state references |
> | 3 | document | Gap Analysis | `wiki/domains/infrastructure/{slug}-gaps.md` | Missing resources, config drift, capacity gaps identified |
> | 4 | design | ADR | `wiki/decisions/{slug}.md` | Provider/service decisions with cost + availability tradeoffs |
> | 5 | design | Resource Spec | `wiki/domains/infrastructure/{slug}-resource-spec.md` | Resource types, sizing, networking, security groups defined |
> | 6 | design | Module Interface Spec | `wiki/domains/infrastructure/{slug}-module-spec.md` | Input variables, output values, module boundaries |
> | 7 | design | Deployment Plan | `wiki/domains/infrastructure/{slug}-deploy-plan.md` | Rollout strategy, rollback procedures, health checks |
> | 8 | scaffold | Variable Definitions | `**/*.tf` (variable blocks) | `terraform validate` passes |
> | 9 | scaffold | Output Definitions | `**/*.tf` (output blocks) | `terraform validate` passes |
> | 10 | scaffold | Module Interface | `modules/**/variables.tf` + `outputs.tf` | Module structure valid |
> | 11 | scaffold | Backend Config | `backend.tf` | `terraform init` succeeds |
> | 12 | implement | Resource Definitions | `**/*.tf` (resource blocks) | `terraform plan` succeeds |
> | 13 | implement | Module Implementation | `modules/**/main.tf` | `terraform validate` |
> | 14 | implement | Environment Wiring | `environments/{env}/main.tf` | Module references resolve |
> | 15 | test | Plan Verification | `terraform plan` output | Plan shows expected changes, no unexpected destroys |
> | 16 | test | Apply (staging) | `terraform apply` output | Apply succeeds in staging environment |
> | 17 | test | Health Checks | endpoint/service checks | Services respond correctly post-apply |
> | 18 | deploy | Production Apply | `terraform apply` (production) | Apply succeeds, health checks pass |
> | 19 | deploy | Runbook | operations-plan page | Operational procedures documented |
> | 20 | deploy | Monitoring Config | alerting/dashboard configs | Monitoring in place before production |

### Scaffold Stage — Infrastructure Specifics

> [!warning] ALLOWED vs FORBIDDEN
>
> **ALLOWED:**
> ```hcl
> # Variable definitions (structure without resources)
> variable "instance_type" {
>   type        = string
>   default     = "t3.medium"
>   description = "EC2 instance type for the application server"
> }
>
> variable "vpc_cidr" {
>   type        = string
>   default     = "10.0.0.0/16"
>   description = "CIDR block for the VPC"
> }
>
> # Output definitions
> output "instance_ip" {
>   value       = "placeholder"
>   description = "Public IP of the application server"
> }
>
> # Module interface (no resources inside yet)
> # modules/app-server/variables.tf
> variable "ami_id" { type = string }
> variable "subnet_id" { type = string }
> ```
>
> **FORBIDDEN:**
> ```hcl
> # Resource blocks (actual infrastructure)
> resource "aws_instance" "app" {    # ← FORBIDDEN in scaffold
>   ami           = var.ami_id
>   instance_type = var.instance_type
> }
>
> # Data sources that query real infrastructure
> data "aws_vpc" "main" {            # ← FORBIDDEN in scaffold
>   default = true
> }
> ```

### Implement Stage — Infrastructure Specifics

> [!tip] Integration = Environment Wiring
>
> In infrastructure, "integration wiring" means: existing environment config references the new module.
>
> ```hcl
> # environments/staging/main.tf (EXISTING file modified)
> module "app_server" {
>   source        = "../../modules/app-server"
>   ami_id        = data.aws_ami.latest.id
>   subnet_id     = module.vpc.public_subnet_ids[0]
> }
> ```
>
> Without this wiring, the module EXISTS but is never USED — the infrastructure equivalent of orphaned code.

### Infrastructure-Specific Artifacts NOT in Code Domains

> [!abstract] Unique to Infrastructure
>
> | Artifact | Purpose | When |
> |----------|---------|------|
> | **State File** | Terraform state tracking real infrastructure | Maintained by Terraform, stored remotely |
> | **Plan Output** | Diff between desired and actual state | Every `terraform plan` run |
> | **Drift Report** | Differences between state and reality | Periodic compliance check |
> | **Cost Estimate** | Projected monthly cost of changes | Before apply, via `infracost` or `terraform plan` |
> | **Runbook** | Step-by-step operational procedures | Before production deployment |
> | **Rollback Plan** | How to undo if apply fails | Part of deployment plan |
> | **Monitoring Config** | Alerts, dashboards, health checks | Before production |

### Other Models — Infrastructure Subsets

> [!abstract] Model → Infrastructure Artifacts
>
> | Model | What Changes |
> |-------|-------------|
> | **Feature Dev** | Full chain — new infrastructure from design to deployment |
> | **Bug Fix** | Document (identify misconfiguration) → Implement (fix resource/variable) → Test (plan + apply staging) |
> | **Hotfix** | Direct fix → plan + apply (emergency, known issue) |
> | **Refactor** | Document (current→target state) → Scaffold (new module structure) → Implement (move resources) → Test (no destroyed resources) |

## Open Questions

> [!question] ~~Should infrastructure projects have a "Deploy" stage beyond "Test"?~~
> **RESOLVED:** Yes — optional domain-specific stage for Infrastructure only. See [[Decision: Methodology Stage Extension Decisions]].

> [!question] ~~How does drift detection fit into the methodology?~~
> **RESOLVED:** Model as periodic monitoring task using bug-fix model. Not a new methodology model. See [[Decision: Methodology Stage Extension Decisions]].

## Relationships

- BUILDS ON: [[Methodology Artifact Taxonomy]]
- BUILDS ON: [[Construction and Testing Artifacts — Standards and Guide]]
- RELATES TO: [[Artifact Chains by Methodology Model]]
- RELATES TO: [[Model: Methodology]]
- RELATES TO: [[Artifact Chain: TypeScript/Node Domain]]
- RELATES TO: [[Artifact Chain: Python/Wiki Domain]]
- FEEDS INTO: [[Methodology Adoption Guide]]

## Backlinks

[[Methodology Artifact Taxonomy]]
[[Construction and Testing Artifacts — Standards and Guide]]
[[Artifact Chains by Methodology Model]]
[[Model: Methodology]]
[[Artifact Chain: TypeScript/Node Domain]]
[[Artifact Chain: Python/Wiki Domain]]
[[Methodology Adoption Guide]]
[[Artifact Chain: Knowledge/Evolution Domain]]
[[Decision: Methodology Stage Extension Decisions]]
[[Universal Stages, Domain-Specific Artifacts]]

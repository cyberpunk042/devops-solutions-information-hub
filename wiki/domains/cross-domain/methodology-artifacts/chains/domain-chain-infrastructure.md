---
title: Artifact Chain — Infrastructure-IaC Domain
aliases:
  - "Artifact Chain — Infrastructure-IaC Domain"
  - "Artifact Chain — Infrastructure/IaC Domain"
  - "Artifact Chain: Infrastructure-IaC Domain"
  - "Artifact Chain: Infrastructure/IaC Domain"
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
    url: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code
tags: [methodology, artifact-chain, infrastructure, terraform, iac, domain-specific, flexible]
---

# Artifact Chain — Infrastructure-IaC Domain
> [!tip] AI Quick Start — Working on Infrastructure as Code
>
> 1. **Identify your context** — Cloud provisioning (Terraform/Pulumi)? Container orchestration (Docker/K8s)? CI/CD pipelines? Config management (Ansible)? Each has different artifacts.
> 2. **Pick your SDLC level** — Simplified: quick provisioning scripts. Default: stage-gated with plan verification. Full: compliance, drift detection, runbooks, monitoring.
> 3. **Scaffold = structure** — Variable/output definitions, module interfaces. NO resource blocks, NO data sources.
> 4. **Implement = resources** — Actual infrastructure definitions + environment wiring.
> 5. **Unique to infra:** Optional deploy stage (production apply), drift detection, state management, cost estimation.

## Summary

Artifact chain resolution for Infrastructure as Code projects (devops-control-plane, Terraform, Docker, CI/CD). Maps methodology stages to IaC-specific artifacts. The unique characteristic of this domain: the "scaffold" stage defines infrastructure STRUCTURE (variables, outputs, module interfaces), the "implement" stage creates RESOURCES (actual infrastructure), and the "test" stage verifies via `terraform plan` and `terraform apply` against a staging environment. State management and drift detection add artifact types not found in code domains.

## Reference Content

### Common Infrastructure Toolchain Options

> [!info] Toolchain varies by project — these are options, not requirements
>
> | Concern | Options | Notes |
> |---------|---------|-------|
> | Provisioning | Terraform, Pulumi, CloudFormation, CDK | Terraform most common, Pulumi for code-first |
> | Containers | Docker, Podman, containerd | Docker dominant, Podman for rootless |
> | Orchestration | Kubernetes, Docker Compose, ECS, Nomad | K8s for production, Compose for dev |
> | Config management | Ansible, Chef, Salt, Shell scripts | Ansible most popular for IaC |
> | CI/CD | GitHub Actions, GitLab CI, Jenkins, ArgoCD | GitOps patterns gaining dominance |
> | State management | S3/GCS backend, Terraform Cloud, local | Remote state required for teams |
> | Cost estimation | Infracost, AWS Calculator, `terraform plan` | Infracost for automated PR cost checks |
> | Drift detection | Terraform plan (periodic), Driftctl, custom | Bug-fix model when drift detected |

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

### SDLC Level Variation

> [!abstract] Artifact Count Varies by SDLC Level
>
> | Stage | Simplified (POC) | Default (Staging) | Full (Production) |
> |-------|-----------------|-------------------|-------------------|
> | **Document** | Informal notes | Req spec + current state + gap analysis | + compliance mapping, security review |
> | **Design** | Quick decisions | ADR + resource spec + module spec + deploy plan | + disaster recovery, capacity plan, cost model |
> | **Scaffold** | Variable stubs | Variables + outputs + module interfaces + backend | + mock environments, test fixtures |
> | **Implement** | Working resources | Resources + modules + environment wiring | + monitoring config, alerting rules |
> | **Test** | Manual plan check | Plan verification + staging apply + health checks | + compliance scan, security audit, load test |
> | **Deploy** | Direct apply | Staging → production with runbook | + blue/green, canary, rollback verification |

### Other Models — Infrastructure Subsets

> [!abstract] Model → Infrastructure Artifacts
>
> | Model | What Changes |
> |-------|-------------|
> | **Feature Dev** | Full chain — new infrastructure from design to deployment |
> | **Bug Fix** | Document (identify misconfiguration) → Implement (fix resource/variable) → Test (plan + apply staging) |
> | **Hotfix** | Direct fix → plan + apply (emergency, known issue) |
> | **Refactor** | Document (current→target state) → Scaffold (new module structure) → Implement (move resources) → Test (no destroyed resources) |

### Ecosystem Examples

> [!example] Validated Implementations
>
> | Project | SDLC Level | Focus | Details |
> |---------|-----------|-------|---------|
> | **devops-control-plane** | Simplified → Default | TUI/CLI/Web + Terraform | [[identity-profile\|devops-control-plane — Identity Profile]] — 24 immune system rules, vault security |

## Open Questions

> [!question] ~~Should infrastructure projects have a "Deploy" stage beyond "Test"?~~
> **RESOLVED:** Yes — optional domain-specific stage for Infrastructure only. See [[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]].

> [!question] ~~How does drift detection fit into the methodology?~~
> **RESOLVED:** Model as periodic monitoring task using bug-fix model. Not a new methodology model. See [[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]].

### How This Connects — Navigate From Here

> [!abstract] From This Page → Related Knowledge
>
> | Direction | Go To |
> |-----------|-------|
> | **What is my identity?** | [[project-self-identification-protocol|Project Self-Identification Protocol — The Goldilocks Framework]] |
> | **What principle applies?** | [[right-process-for-right-context-the-goldilocks-imperative|Principle — Right Process for Right Context — The Goldilocks Imperative]] |
> | **Full artifact taxonomy** | [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]] (78 types across 11 categories) |
> | **Generic chains by model** | [[artifact-chains-by-model|Artifact Chains by Methodology Model]] |
> | **SDLC levels** | [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]] |
> | **System map** | [[methodology-system-map|Methodology System Map]] |

## Relationships

- BUILDS ON: [[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
- BUILDS ON: [[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
- RELATES TO: [[artifact-chains-by-model|Artifact Chains by Methodology Model]]
- RELATES TO: [[model-methodology|Model — Methodology]]
- RELATES TO: [[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
- RELATES TO: [[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
- RELATES TO: [[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
- FEEDS INTO: [[methodology-adoption-guide|Methodology Adoption Guide]]

## Backlinks

[[methodology-artifact-taxonomy|Methodology Artifact Taxonomy]]
[[construction-and-testing-artifacts|Construction and Testing Artifacts — Standards and Guide]]
[[artifact-chains-by-model|Artifact Chains by Methodology Model]]
[[model-methodology|Model — Methodology]]
[[sdlc-customization-framework|SDLC Customization Framework — Phases, Scale, and Chain Selection]]
[[domain-chain-typescript|Artifact Chain — TypeScript-Node Domain]]
[[domain-chain-python-wiki|Artifact Chain — Python-Wiki Domain]]
[[methodology-adoption-guide|Methodology Adoption Guide]]
[[domain-chain-knowledge|Artifact Chain — Knowledge-Evolution Domain]]
[[methodology-stage-extension-decisions|Decision — Methodology Stage Extension Decisions]]
[[universal-stages-domain-specific-artifacts|Universal Stages, Domain-Specific Artifacts]]

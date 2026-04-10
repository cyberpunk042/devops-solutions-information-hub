# DevOps

The operational backbone: stage-gate methodology, ecosystem topology, backlog management, task governance, infrastructure patterns, and the control plane vision. This domain defines how work proceeds across all projects.

**Model:** [[Model: Methodology]] | **Standards:** [[Methodology Standards — What Good Execution Looks Like]]

### Start Here

1. [[Stage-Gate Methodology]] — The 5-stage sequential system governing all work
2. [[Four-Project Ecosystem]] — The personal devops infrastructure topology
3. [[Task Type Artifact Matrix]] — The 7 task types and their required artifacts

### Methodology

| Page | What it covers |
|------|---------------|
| [[Stage-Gate Methodology]] | Document → Design → Scaffold → Implement → Test |
| [[Task Type Artifact Matrix]] | 7 task types: epic, module, task, bug, hotfix, spike, chore |
| [[Backlog Hierarchy Rules]] | EPIC → MODULE → TASK three-level structure |
| [[Execution Modes and End Conditions]] | Operational envelope for autonomous agent execution |
| [[Immune System Rules]] | 24 governance rules from 16 post-mortems |

### Ecosystem and Infrastructure

| Page | What it covers |
|------|---------------|
| [[Four-Project Ecosystem]] | openfleet, AICP, DSPD, devops-control-plane |
| [[devops-control-plane]] | Unified solution management platform |
| [[Infrastructure as Code Patterns]] | IaC beyond Terraform: config-as-code in the ecosystem |
| [[WSL2 Development Patterns]] | Linux dev ecosystem alongside Windows tools |

## Pages

- [Backlog Hierarchy Rules](backlog-hierarchy-rules.md) — The Backlog Hierarchy Rules define the three-level EPIC → MODULE → TASK structure used by the OpenArms project and mi...
- [devops-control-plane](devops-control-plane.md) — The devops-control-plane is a unified solution management platform that provides one place to see, manage, and evolve...
- [Execution Modes and End Conditions](execution-modes-and-end-conditions.md) — Execution Modes and End Conditions define the operational envelope for autonomous agent execution in the OpenArms met...
- [Four-Project Ecosystem](four-project-ecosystem.md) — The four-project ecosystem is a personal devops infrastructure built by a single engineer running a fleet of AI agent...
- [Immune System Rules](immune-system-rules.md) — The Immune System Rules are 24 operational governance rules derived from 16 post-mortems and agent death analyses, co...
- [Infrastructure as Code Patterns](infrastructure-as-code-patterns.md) — Infrastructure as Code (IaC) in the four-project ecosystem extends beyond Terraform and Ansible into a pattern where ...
- [Stage-Gate Methodology](stage-gate-methodology.md) — Stage-Gate Methodology is the 5-stage sequential system — Document → Design → Scaffold → Implement → Test — that gove...
- [Task Type Artifact Matrix](task-type-artifact-matrix.md) — The Task Type Artifact Matrix defines the 7 distinct task types in the OpenArms methodology — epic, module, task, bug...
- [WSL2 Development Patterns](wsl2-development-patterns.md) — WSL2 (Windows Subsystem for Linux 2) enables running a full Linux development ecosystem alongside Windows tools, but ...

## Tags

`devops`, `openarms`, `openfleet`, `epic`, `module`, `task`, `readiness`, `quality-gates`, `methodology`, `backlog`, `hierarchy`, `status-propagation`, `wiki-backlog`, `task-management`, `decomposition`, `upward-aggregation`, `control-plane`, `project-management`, `tech-detection`, `vault`

## Cross-Platform App Port v0.2.0

This release strengthens the skill for real, long-running app migrations while keeping small feature ports lightweight.

### What’s new

- **Workflow scaling** — use compact artifacts for a small feature, a fuller workspace for a subsystem, and the complete migration package for an app-wide port.
- **Controlled loop execution** — bounded and multi-agent runs now require objective verification, explicit limits, reversible workspaces, and recorded terminal reasons.
- **Commit-bound evidence** — a completed slice must identify the target commit and verification time used for its evidence.
- **Independent verification guidance** — high-risk or unattended work can use a separate verifier without allowing subjective review to override failing tests or builds.
- **Human approval gates** — merge, deployment, app-store submission, credential rotation, destructive migrations, and similar difficult-to-reverse actions require explicit approval.
- **Improved migration state** — schema `1.1` adds run controls, evidence freshness fields, and validator enforcement.
- **Bird’s-eye workflow diagrams** — both READMEs now show the complete porting flow and controlled iteration loop.
- **Reproducible eval reporting** — eval guidance now records the agent, model, environment, skill commit, assertion-level evidence, efficiency, and failures.

### Validation

The bundled validators check the Agent Skill package structure and the migration-state template. The included agent evals remain test definitions until they are executed in clean sessions with and without the skill.

### Install

```bash
npx skills add https://github.com/Xilantra/skills --skill cross-platform-app-port
```

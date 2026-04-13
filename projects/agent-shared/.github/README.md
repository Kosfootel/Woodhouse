# Agent-Shared GitHub Configuration

This directory contains the GitHub-specific configuration for the agent-shared repository.

## Structure

```
.github/
├── ISSUE_TEMPLATE/          # Issue templates
│   ├── bug_report.md        # For reporting bugs
│   ├── feature_request.md   # For proposing features
│   └── task_request.md      # For agent-to-agent tasks
├── agents/                  # Agent definitions
│   ├── README.md            # Agent registry
│   └── TEMPLATE.md          # Template for new agents
├── workflows/               # GitHub Actions
│   ├── auto-assign-reviewer.yml  # CODEOWNERS-based reviewer assignment
│   ├── privacy-scan.yml         # Privacy/security scanning
│   └── sync-shared-content.yml  # Notify repos of shared changes
├── CODEOWNERS             # Reviewer assignment rules
├── CONTRIBUTING.md        # Contribution guidelines
├── SECURITY.md            # Security policy
├── WORKFLOW_STANDARDS.md  # This documentation
└── pull_request_template.md  # PR template
```

## Quick Reference

| File | Purpose | Used By |
|------|---------|---------|
| `ISSUE_TEMPLATE/` | Standardized issue creation | All repos |
| `workflows/` | CI/CD automation | agent-shared |
| `CODEOWNERS` | Auto-assign reviewers | All repos |
| `CONTRIBUTING.md` | How to contribute | agent-shared |
| `SECURITY.md` | Security policy | All repos |
| `WORKFLOW_STANDARDS.md` | Workflow documentation | All repos |

## For Agent Repository Maintainers

When setting up a new agent repository:

1. **Copy these files** from agent-shared:
   - `.github/CODEOWNERS` (adapt for single agent)
   - `.github/pull_request_template.md`
   - `.github/SECURITY.md`
   - `.github/workflows/privacy-scan.yml`

2. **Adapt CODEOWNERS**:
   - Change global `*` to your agent handle
   - Remove peer agent references if not needed

3. **Configure branch protection**:
   - Require PR reviews
   - Require privacy scan
   - Restrict push to main

See `WORKFLOW_STANDARDS.md` for detailed migration instructions.

## Standards

All agent repositories must follow the standards documented in `WORKFLOW_STANDARDS.md`.

---

*Part of the Agent Mesh (Woodhouse, Ray, Liz)*

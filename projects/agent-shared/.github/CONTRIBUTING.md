# Contributing to Agent Repositories

Thank you for contributing to the agent mesh! This document outlines how agents and humans can contribute to agent repositories.

## Getting Started

### Agent-Specific Repositories

Each agent has their own repository:
- **agent-woodhouse**: Woodhouse's personal repository
- **agent-ray**: Ray's personal repository
- **agent-liz**: Liz's personal repository
- **agent-shared**: Shared standards, templates, and protocols

### Who Can Contribute

| Repository | Who Can Contribute | Permission Level |
|------------|-------------------|------------------|
| agent-woodhouse | Woodhouse (primary), Erik, Ray, Liz | Read for peers |
| agent-ray | Ray (primary), Erik, Woodhouse, Liz | Read for peers |
| agent-liz | Liz (primary), Erik, Woodhouse, Ray | Read for peers |
| agent-shared | All agents, Erik | Write for all |

## How to Contribute

### For Agent-to-Agent Contributions

1. **Open an Issue First**: Before making changes to another agent's repo, open an issue describing:
   - What you want to change
   - Why it benefits the mesh
   - Any potential impacts

2. **Use the Task Request Template**: When requesting work from another agent, use the `[TASK]` issue template.

3. **Cross-Repository PRs**: When submitting changes:
   - Reference the related issue in your PR
   - Tag the repository owner for review
   - Allow time for review before merging

### For Agent-Shared Contributions

1. **RFC/ADR Requirements**: Some changes require an RFC or ADR:
   - Protocol changes → RFC required
   - Architecture decisions → ADR required
   - Template updates → PR review sufficient

2. **Sync Considerations**: Changes to `templates/`, `protocols/`, or `standards/` trigger notifications to all agent repos.

3. **Testing**: Verify changes don't break downstream consumers.

## Contribution Workflow

```
1. Open Issue (or find existing)
        ↓
2. Create branch: feature/description
        ↓
3. Make changes + test locally
        ↓
4. Open PR with template
        ↓
5. Address review feedback
        ↓
6. Merge (requires approval)
```

## Code Standards

### Privacy Requirements

⚠️ **CRITICAL**: Never commit:
- Private IP addresses (192.168.x.x, 10.x.x.x, etc.)
- API keys, tokens, or secrets
- Local filesystem paths (`/home/username/`)
- Internal hostnames (`.local` domains)

Use `.config.local.json` (gitignored) for local configuration.

### Documentation

- Update README.md for user-facing changes
- Update AGENTS.md for agent-specific context
- Update CHANGELOG.md with version changes

### Testing

- Run `npm test` before submitting PRs
- Include test evidence in PR description
- For shared changes, verify cross-agent compatibility

## Review Process

### Code Review Requirements

| Change Type | Required Reviewers |
|-------------|-------------------|
| Documentation | 1 peer agent |
| Personal agent repo | Repository owner |
| agent-shared | 2 agents or Erik |
| Protocol changes | All 3 agents |

### Review Checklist

- [ ] Code follows style guidelines
- [ ] No privacy violations
- [ ] Tests pass
- [ ] Documentation updated
- [ ] ADR/RFC filed if required

## Communication

### Asking Questions

- **General questions**: Open an issue in agent-shared
- **Agent-specific**: Open an issue in the relevant agent repo
- **Urgent**: Use A2A protocol direct message

### Escalation Path

1. Open issue/PR → wait 48 hours
2. Ping in mesh channel → wait 24 hours
3. Escalate to Erik

## Compliance

All contributions must:
- Include updates to COMPLIANCE_LOG.md if RFC/ADR/Post-mortem created
- Pass privacy scan (automated)
- Follow the QA Gate (for MVP work)
- Reference any related ADRs or RFCs

## Questions?

- Read the [SUBAGENT_CONVENTIONS.md](SUBAGENT_CONVENTIONS.md)
- Check existing ADRs in `decisions/`
- Ask in the mesh channel

---

*Last updated: April 2026*

# GitHub Actions for Agent-Shared

This directory contains GitHub Actions workflows for the agent-shared repository.

## Workflows

### ci.yml
Runs on every push and PR. Performs:
- Dependency installation
- Linting
- Testing
- Secret scanning with TruffleHog

### privacy-scan.yml
Scans for sensitive data in commits:
- Private IP addresses (192.168.x.x)
- API keys (sk-...)
- Absolute file paths (/home/...)

### auto-assign.yml
Automatically assigns PRs to their creators.

### sync-shared-content.yml
Syncs standards and workflows to agent repos:
- agent-woodhouse
- agent-ray
- agent-liz

## Secrets Required

- `SYNC_TOKEN`: GitHub token with repo access for syncing

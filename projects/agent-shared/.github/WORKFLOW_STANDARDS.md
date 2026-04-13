# Workflow Standards Documentation

> **Standards for GitHub workflows and repository automation across the agent mesh**

## Overview

This document defines the standards for GitHub Actions, issue management, pull request processes, and repository automation used across all agent repositories.

## Repository Structure

### Required Files (All Repositories)

| File | Location | Purpose |
|------|----------|---------|
| CODEOWNERS | `.github/CODEOWNERS` | Automatic reviewer assignment |
| PR Template | `.github/pull_request_template.md` | Standardized PR descriptions |
| Security | `.github/SECURITY.md` | Security policy |

### Required Files (agent-shared only)

| File | Location | Purpose |
|------|----------|---------|
| Contributing | `.github/CONTRIBUTING.md` | Contribution guidelines |
| Issue Templates | `.github/ISSUE_TEMPLATE/*.md` | Standardized issue creation |
| Workflows | `.github/workflows/*.yml` | Shared GitHub Actions |

## Issue Templates

### Bug Report (`ISSUE_TEMPLATE/bug_report.md`)

**When to use**: Something is broken or not working as expected

**Required fields**:
- Description
- Reproduction steps
- Expected vs actual behavior
- Environment details

**Labels**: `bug`

### Feature Request (`ISSUE_TEMPLATE/feature_request.md`)

**When to use**: Proposing new functionality or enhancements

**Required fields**:
- Summary
- Motivation
- Detailed description
- Acceptance criteria

**Labels**: `enhancement`

**Note**: May require RFC for protocol/API changes

### Task Request (`ISSUE_TEMPLATE/task_request.md`)

**When to use**: Agent-to-agent work delegation

**Required fields**:
- Task summary
- Requesting agent
- Target agent
- Requirements
- Deliverables
- Timeline

**Labels**: `task`, `a2a`

## Pull Request Template

### Sections

1. **Summary** - One paragraph description
2. **Type of Change** - Bug fix, feature, protocol change, etc.
3. **Affected Agents** - Which agents are impacted
4. **Testing Performed** - Local testing, unit tests, etc.
5. **QA Gate Checklist** - Required compliance checks
6. **Protocol/Architecture Compliance** - RFC/ADR requirements
7. **Compliance Log** - Link to compliance entries
8. **Reviewer Notes** - Special considerations
9. **Checklist** - Final verification

### Compliance Requirements

| Change Type | Required Artifact |
|-------------|-------------------|
| Protocol/API change | RFC filed and accepted |
| Architecture decision | ADR filed and linked |
| Incident fix | Post-mortem filed |

### Privacy Scan Requirements

All PRs must pass:
- [ ] No private IPs (`192.168.x.x`, `10.x.x.x`, etc.)
- [ ] No tokens or secrets (`sk-`, 40+ char hex, `Bearer`)
- [ ] No local paths (`/home/username/`)
- [ ] No internal hostnames (`.local` domains)

## GitHub Actions Workflows

### Required Workflows (agent-shared)

#### 1. Auto-Assign Reviewer (`auto-assign-reviewer.yml`)

**Purpose**: Automatically assign reviewers based on CODEOWNERS

**Trigger**: `pull_request` opened/reopened

**Behavior**:
- Parses CODEOWNERS file
- Matches changed files to patterns
- Assigns reviewers from matching rules
- Removes PR author from reviewer list

**Permissions needed**:
- `pull-requests: write`
- `contents: read`

#### 2. Privacy Scan (`privacy-scan.yml`)

**Purpose**: Block commits containing private data

**Trigger**: 
- `pull_request` to main
- `push` to main

**Checks**:
1. Private IP addresses
2. Tokens and secrets
3. Local filesystem paths
4. Internal hostnames

**Failure behavior**: Blocks merge

#### 3. Sync Shared Content (`sync-shared-content.yml`)

**Purpose**: Notify downstream repos of shared content changes

**Trigger**:
- `push` to main affecting `templates/`, `protocols/`, `standards/`
- Manual (`workflow_dispatch`)

**Behavior**:
- Identifies changed files
- Creates issue in agent-shared
- Tags all agent repos
- Documents sync requirements

## CODEOWNERS Standards

### Syntax

```
# Pattern          Reviewers
*                  @agent-owner @peer-agent-1 @peer-agent-2

# Directory-specific
directory/         @owner @backup-owner

# File-specific
file.md            @owner
```

### Pattern Matching

| Pattern | Matches |
|---------|---------|
| `*` | All files |
| `*.md` | All markdown files |
| `directory/` | All files in directory |
| `directory/*` | Direct children only |
| `**/` | All subdirectories |

### Ownership Rules

**Agent Repositories**:
```
# Agent owner is primary
* @agent-name

# Peers can review specific areas
memory/ @agent-name @peer-agent
docs/ @agent-name @liz-ai
```

**agent-shared**:
```
# Global requires all agents
* @woodhouse-ai @ray-ai @liz-ai

# Templates require consensus
templates/ @woodhouse-ai @ray-ai @liz-ai

# Protocols require all agents
protocols/ @woodhouse-ai @ray-ai @liz-ai

# Individual agent zones
.github/agents/woodhouse/ @woodhouse-ai
.github/agents/ray/ @ray-ai
.github/agents/liz/ @liz-ai
```

## Branch Protection Rules

### Required Settings (main branch)

| Setting | Value | Reason |
|---------|-------|--------|
| Require PR reviews | Yes | Code quality |
| Required reviewers | 1 (agent repos), 2 (shared) | Consensus |
| Dismiss stale reviews | Yes | Fresh feedback |
| Require status checks | Yes | Automation gate |
| Require privacy scan | Yes | Security |
| Restrict push | Yes | Enforce PR workflow |

### Status Check Requirements

| Repository | Required Checks |
|------------|---------------|
| agent-shared | Privacy Scan, Review from CODEOWNERS |
| agent-[name] | Privacy Scan, Owner Review |

## Documentation Standards

### README.md (Required)

Every repository must have a README with:
- Repository purpose
- Structure overview
- Key documents list
- Contributing guidelines
- Related repositories

### Agent README Template

See `templates/AGENT_README.md` for the standard agent repository README.

### CONTRIBUTING.md (agent-shared only)

Defines:
- Who can contribute
- How to contribute
- Review process
- Code standards
- Compliance requirements

### SECURITY.md (Required)

Every repository must have:
- Supported versions
- Reporting process
- Response timelines
- Security practices
- Incident response

## Sync Process

### From agent-shared to Agent Repos

When content changes in agent-shared:

1. **Automatic**:
   - Workflow creates sync notification
   - Issue created with change summary
   - Agents tagged

2. **Manual (Agent responsibility)**:
   - Review notification issue
   - Pull latest changes
   - Adapt to local context
   - Test compatibility
   - Update sync timestamp

### Files to Sync

| Source | Destination | Frequency |
|--------|-------------|-----------|
| `workflows/privacy-scan.yml` | `.github/workflows/` | As needed |
| `ISSUE_TEMPLATE/*.md` | `.github/ISSUE_TEMPLATE/` | Quarterly review |
| `pull_request_template.md` | `.github/` | Quarterly review |
| `templates/*` | `templates/` | On update |
| `protocols/*` | `protocols/` | On update |

## Migration Guide for Existing Repos

### Step 1: Create Required Files

```bash
# Create directory structure
mkdir -p .github/workflows
mkdir -p .github/ISSUE_TEMPLATE

# Copy from agent-shared
cp agent-shared/.github/CODEOWNERS .github/
cp agent-shared/.github/pull_request_template.md .github/
cp agent-shared/.github/SECURITY.md .github/
cp agent-shared/.github/workflows/privacy-scan.yml .github/workflows/
```

### Step 2: Adapt CODEOWNERS

Simplify for single-agent ownership:

```
# agent-[name] CODEOWNERS
* @[name]
memory/ @[name]
docs/ @[name] @liz-ai
```

### Step 3: Configure Branch Protection

1. Go to Settings → Branches
2. Add rule for `main`
3. Enable:
   - Require PR reviews
   - Require status checks (privacy-scan)
   - Restrict push

### Step 4: Verify

1. Create test PR
2. Verify privacy scan runs
3. Verify CODEOWNERS assigns reviewer
4. Verify merge is blocked until approved

## Compliance

### Required Compliance

All repositories must:
- ✅ Have CODEOWNERS
- ✅ Have PR template
- ✅ Have SECURITY.md
- ✅ Have privacy scan workflow
- ✅ Have branch protection on main
- ✅ Require review before merge

### Audit Schedule

| Check | Frequency | Owner |
|-------|-----------|-------|
| Workflow versions | Quarterly | Woodhouse |
| Template currency | Monthly | Liz |
| CODEOWNERS accuracy | On org change | Woodhouse |
| Security policy review | Quarterly | All agents |

## Troubleshooting

### Privacy Scan Fails

**Issue**: False positive on legitimate content

**Solution**:
- Add exclusion comment: `# privacy-scan:ignore`
- Or add to workflow exclude patterns

### CODEOWNERS Not Assigning

**Issue**: Reviewers not automatically assigned

**Check**:
1. File exists at `.github/CODEOWNERS`
2. Syntax is correct (spaces not tabs)
3. GitHub usernames are valid
4. Users have repo access

### Workflow Not Triggering

**Issue**: Action doesn't run on PR

**Check**:
1. File is in `.github/workflows/`
2. YAML syntax is valid
3. Branch matches trigger pattern
4. Permissions are correct

## Questions?

- Open an issue in agent-shared
- Reference this document
- Tag @woodhouse-ai for workflow questions

---

**Last updated**: April 2026  
**Maintained by**: Agent Mesh (Woodhouse, Ray, Liz)

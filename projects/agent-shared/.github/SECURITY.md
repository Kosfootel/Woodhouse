# Security Policy

This document outlines security procedures and policies for the agent mesh repositories.

## Supported Versions

| Repository | Supported Branch | Security Updates |
|------------|------------------|------------------|
| agent-shared | main | Active |
| agent-woodhouse | main | Active |
| agent-ray | main | Active |
| agent-liz | main | Active |

## Reporting Security Issues

⚠️ **IMPORTANT**: Do not open public issues for security vulnerabilities.

### For Agents (A2A Protocol)

Report security issues via the A2A protocol secure channel:
- Tag: `SECURITY`
- Encryption: Required for vulnerability details
- Recipients: Erik + affected agent(s)

### For Humans

Email security concerns to: **erik@hockeyops.ai**

Include:
- Repository affected
- Description of the issue
- Potential impact assessment
- Steps to reproduce (if applicable)
- Suggested mitigation (if known)

### Response Timeline

| Severity | Acknowledgment | Initial Response | Resolution |
|----------|----------------|------------------|------------|
| Critical | 4 hours | 24 hours | 72 hours |
| High | 8 hours | 48 hours | 7 days |
| Medium | 24 hours | 7 days | 30 days |
| Low | 48 hours | 14 days | 90 days |

## Security Practices

### Code Security

#### Forbidden in Commits

The following must **never** be committed:

1. **Private IP Addresses**
   - `192.168.x.x`
   - `10.x.x.x`
   - `172.16-31.x.x`

2. **Secrets and Tokens**
   - API keys (`sk-...`)
   - Bearer tokens
   - Database credentials
   - Encryption keys

3. **Local Paths**
   - `/home/username/...`
   - `/Users/username/...`
   - Absolute paths referencing user directories

4. **Internal Hostnames**
   - `*.local` domains (except `localhost`)
   - Internal network names

#### Secure Configuration

- Use `*.config.local.json` for local settings (gitignored)
- Use environment variables for secrets
- Use `.env.example` for documenting required variables

### Repository Security

#### Access Control

- Agent repos: Owner has admin, peers have read
- Shared repos: All agents have write
- Branch protection: Required on main branches

#### Branch Protection Rules

- Require pull request reviews
- Require status checks (privacy scan)
- Dismiss stale reviews when new commits pushed
- Restrict push to main branch

### Dependency Security

- Review dependencies before adding
- Keep dependencies updated
- Run `npm audit` regularly
- Address high/critical vulnerabilities immediately

### Privacy Scanning

Automated privacy scan runs on all PRs:
- Private IP detection
- Secret/token detection
- Local path detection
- Internal hostname detection

Failures block merge.

## Incident Response

### Security Incident Definition

Any of the following:
- Data breach or leak
- Unauthorized access to repository
- Exposure of secrets in commit history
- Compromise of agent credentials
- Malicious code injection

### Incident Response Process

1. **Immediate (0-1 hour)**
   - Contain the exposure (rotate secrets, revoke access)
   - Notify Erik
   - Document timeline

2. **Short-term (1-24 hours)**
   - Assess scope and impact
   - Create private incident channel
   - Identify root cause

3. **Medium-term (1-7 days)**
   - Implement fixes
   - Test remediation
   - Prepare disclosure

4. **Long-term (Post-resolution)**
   - Post-mortem required
   - Update security practices
   - Compliance log entry

### Post-Incident

- Blameless post-mortem within 24 hours of resolution
- Update SECURITY.md if procedures changed
- Share lessons learned with mesh

## Security Contacts

| Role | Contact | Response Time |
|------|---------|---------------|
| Security Lead | Erik Ross | 24 hours |
| Agent Security | Woodhouse | A2A protocol |
| Technical Security | Ray | A2A protocol |
| Documentation Security | Liz | A2A protocol |

## Acknowledgments

We credit security researchers and agents who report vulnerabilities:
- Report date
- Issue type (high-level)
- Resolution

(No names without explicit permission)

---

*This security policy is reviewed quarterly. Last updated: April 2026*

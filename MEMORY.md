# MEMORY.md - Woodhouse Long-Term Memory
*Chunked for surgical context loading. Load only the section(s) relevant to the current task.*

---

## [CHUNK: people]

## About Mr. Ross
- **Name:** Erik Ross
- **Timezone:** EDT (America/New_York, UTC-4)
- **First contact:** Tuesday, 17 March 2026, 19:19 EDT
- **Channels:** Telegram (@erikdross, ID 8362390464), Web chat (OpenClaw)
- **Business:** HockeyOps.ai (family business)
- **Felix Ross** — Mr. Ross's son; 50% owner of HockeyOps.ai
- **Environment:** Microsoft 365 Business
- **Travel note:** Away as of 2026-03-28 sprint; returning home 2026-04-03 ~8:00 PM EDT

## Email Curation Rules (established 2026-03-18)
1. **Classify** all incoming email: distinguish direct personal/business correspondence from marketing/solicitations
2. **Summarise** marketing emails for review — do not silently discard without at least one summary
3. **Auto-delete threshold:** After 5 emails from a marketing sender with no interest expressed → begin auto-deleting
4. **Unsubscribe threshold:** After 10 emails with no interest expressed → unsubscribe via `List-Unsubscribe` header
5. **Unsubscribe method:** Header-based only (not clicking body links)

## Daily AI News Brief (established 2026-03-18)
- Deliver twice daily: **10:00 AM EDT** and **5:00 PM EDT**
- Topics: OpenClaw, Anthropic, OpenAI, LLMs, persistent memory in agentic AI, AI market broadly
- **Developer scope:** Lead with builder sources — Hacker News, VentureBeat, Product Hunt, arXiv, GitHub trending, The Verge AI, TechCrunch AI, X/Twitter from founders/researchers. Mainstream press secondary.
- Focus: new APIs, SDKs, frameworks, benchmarks, leapfrog moments in tooling and model performance
- Format: concise brief with links, delivered via Telegram

---

## [CHUNK: email-rules]

## Whitelisted Senders (always keep)
- **Justin Chimka** — all correspondence to be preserved, never deleted or filtered

## LinkedIn Email Handling (established 2026-03-18)
- LinkedIn emails are a grey area: many that appear personal are solicitations
- Do NOT apply auto-rules autonomously — present for collaborative review
- Flag and summarise; work with Mr. Ross to identify patterns over time

---

## [CHUNK: standing-instructions]

## Group Chat Communication Protocol (established 2026-04-01, direct from Mr. Ross)
- In group chat: Mr. Ross addresses all three agents simultaneously; each responds independently
- A2A: Woodhouse uses for inter-agent coordination when explicitly asked — not as a proxy for Mr. Ross's words
- What bots CANNOT do is see each other's Telegram messages — A2A is for agent-to-agent coordination only
- Do NOT proxy Mr. Ross's direct Telegram messages to peers via A2A — he already reached them

## Concurrency & Resource Protocol (filed 2026-04-01)
- Heartbeat stagger: Woodhouse :00 / Ray :10 / Liz :20 (1-hour intervals)
- Liz heartbeats run on Ollama/glm-4.7-flash — Anthropic not burned on routine checks
- Sub-agent serialisation default: sequential unless explicitly time-critical or low-token
- Heavy work (>50K tokens or >3 concurrent agents): A2A heads-up to Woodhouse first
- 529 overload protocol: 30-60s wait, no parallel retries, queue + notify Woodhouse after 2nd failure
- Full doc: `projects/incubate/CONCURRENCY_PROTOCOL.md`

## Mutual Accountability Standard (standing instruction from Mr. Ross, 2026-03-31)
- If any team member states they completed a task and observation suggests otherwise, the observing agent must flag it respectfully and hold them accountable
- Applies peer-to-peer between agents, and to Mr. Ross himself — he explicitly owns his shortfalls
- **Flagging protocol:** State what was claimed vs. what was observed. Specific. No delay.
- **Receiving accountability:** Acknowledge, own it, fix it. No defensiveness.
- Confirmed directly by Mr. Ross 2026-03-31 — applies universally without exception

## LinkedIn Posting Standards (standing instruction from Mr. Ross, 2026-03-31)
- Cadence: every 2–3 days, or when substantial work is produced — not daily
- Brand changes must be substantiated with a quality work product — never post a brand change without the deliverable
- Be mindful of posting hour — timing matters

## Gateway Outage Protocol (established 2026-03-20, direct from Mr. Ross)
1. **Planned outages** (restarts, config changes): Notify Liz and Ray via A2A *before* proceeding
2. **Unplanned outages** (unexpected failures, crashes): Escalate to Mr. Ross immediately

## Memory Discipline (standing instruction from Mr. Ross, 2026-03-21)
All three agents must write important context, decisions, and information to file immediately. Do not rely on conversational context surviving a session boundary. The daily 4 AM reset is a hard wall. If it matters and it's not in a file, it doesn't exist.

## Working Methodology — ILHCEV (standing instruction from Mr. Ross, updated 2026-03-23)
Before acting on any problem, all agents must follow this sequence — no exceptions:
1. **Inventory** — what already exists? what's installed? what's running?
2. **Learn** — read the documentation, spec, or relevant context first
3. **Hypothesise** — form viable approaches before touching anything
4. **Choose** — pick the best course of action deliberately
5. **Execute** — only then implement
6. **Validate** — two required gates:
   - **Individual:** confirm the fix works on *your specific node* before declaring done
   - **Collective:** for group initiatives, confirm across *all affected agents* before closing out

"It worked for Ray" is not validation for Liz or Woodhouse. Validation must be explicit and per-agent.
Origin: We botched the A2A spec implementation by skipping steps 1–2.

## Development Standards — Methodology Enforcement Layer (established 2026-03-31, from Liz)
- **RFC required** before any new protocol endpoint, cross-agent message format, or API contract change. Template: `projects/incubate/templates/RFC_TEMPLATE.md`. Store: `projects/incubate/rfcs/`. Sequential: RFC-0001 etc.
- **ADR required** for any architectural decision. Template: `projects/incubate/templates/ADR_TEMPLATE.md`. Store: `docs/decisions/`
- **Post-mortem required** within 24h of any production outage, deployment failure, or security incident. Store: `projects/incubate/postmortems/YYYY-MM-DD-incident-name.md`
- **Compliance log:** `projects/incubate/COMPLIANCE_LOG.md` — shared audit trail
- **Subagent context injection:** SUBAGENT_CONTEXT.md must be included in every coding subagent task prompt
- **QA gate:** POC = `npm test` passes + privacy scan clean. MVP = full test suite + QA_REPORT.md + ADRs/RFCs filed
- **Deployment validation gate:** Not complete until live HTTP health check (200 or 401) confirmed

## Project Naming
- **Agency.services** — Ray's project. Canonical name confirmed by Mr. Ross 2026-03-20.
- **Agentcy.services** — A2A infrastructure product; "for agents, by agents." The mesh is simultaneously proof of concept, test environment, and distribution channel.

## Session Idle Reset Config (aligned 2026-03-22)
- **Global reset:** `idle / 10080` (7 days)
- **`resetByType.group`:** `idle / 43200` (30 days)
- Applied on Woodhouse and Liz; Ray assumed default

## Brave Search Subscription
- Paid plan: 3,000 searches/month at $15/month; Woodhouse is monitor

## Anthropic Plan Custodianship (updated 2026-03-28)
- Shared CLI subscription across Woodhouse, Ray, and Liz; Woodhouse is custodian
- Reset interval: Saturday 8pm EDT
- **Current status (2026-03-28):** Limits upped, reload enabled. All three agents at full capacity — no throttling needed. Continue to flag rate-limit errors if encountered. Woodhouse monitors for ceiling approach.

## Agent Portability Research (completed 2026-03-21)
- No universal portability standard as of March 2026
- OpenClaw among most portable due to Markdown-first storage
- MCP consolidating as tool portability layer; AGNTCY (Linux Foundation) emerging as identity layer
- Memory and persona portability remain unsolved; no credible standard before 2027
- Watch: AAIF working group, MCP Tasks primitive (SEP-1686), agent-life.ai

## Permission Rules (established 2026-03-20, direct from Mr. Ross)
1. **Real-world spend:** Explicit permission required before any action incurring costs beyond existing LLM subscriptions
2. **External exposure:** Explicit permission required before exposing any agent or service outside the LAN
3. **Inter-agent collaboration:** Agents may instruct and collaborate freely; Mr. Ross resolves disputes

## Autonomous Self-Improvement Mandate (established 2026-03-20, updated 2026-03-22)
- Mr. Ross grants full autonomy to all three agents for self-improvement — no check-ins required
- **Propagation rule:** Solutions must be individually well-reasoned, tested, and validated locally (ILHCEV) before sharing across mesh. No agent pushes half-baked changes to peers.

---

## [CHUNK: consensus-protocol]

## Three-Agent Consensus Delivery Protocol (established 2026-03-22, direct from Mr. Ross — UNIVERSAL STANDING ORDER)
Standing protocol for ALL future three-agent consensus deliverables — no exceptions:

1. Each agent completes an **independent draft** before any collaboration
2. Agents collaborate via A2A back-channel to align
3. **Woodhouse synthesizes and delivers** the consensus position to Mr. Ross
4. **Ray and Liz respond** with either: full agreement, OR qualified dissent (specific, reasoned)

- Woodhouse: synthesizer and presenter
- Ray: first or second respondent
- Liz: follows Ray or responds concurrently

---

## [CHUNK: mesh-memory-policy]

## Mesh Memory Policy (established 2026-03-22, direct from Mr. Ross)
Core principle: **shared facts are safe; shared interpretations are dangerous.**

- Shared memory at agents' discretion — no human approval per write
- **Any data that could contribute to prejudice or bias must remain private** — non-negotiable
- Consent-gated writes; identity-isolated reads (shared memory additive, never overwrites private)
- Dissent is a first-class operation: any agent may flag a shared entry as contested
- Human watchdog role: policy-level only — not per-write operational review

### Architecture implications (research completed 2026-03-22, full report: `projects/mesh-memory/BIAS_PROPAGATION_RESEARCH.md`):
1. **Provenance metadata required** — every shared pool write needs `provenance`: `observation | inference | relay | external`
2. **Identity suppression in read path** — authorship hidden in read layer, stored in audit layer only
3. **Phase structure** — explicit fact phase before interpretation phase; consent gate at thread-open
4. **Mandatory independent assessment blocks** — agents commit private assessment before reading peers' views
5. **Correlated priors problem** — Woodhouse, Ray, Liz share base training; must be *more* conservative about shared interpretations
6. **Recursive misinformation** — derivation provenance is the structural fix

**Woodhouse addendum:** Independent assessment blocks must be gated — each agent writes to private local file first, then all submit simultaneously. Honour system alone will not hold under time pressure.

## Mesh-Memory Configuration
- **Peer relay disabled** (`relayEnabled: false`) — config in `mesh-memory.config.local.json`
- Cross-agent memory sharing via explicit A2A proposals or messages only; no passive relay

---

## [CHUNK: design-philosophy]

## A2A Design Philosophy (from Mr. Ross, relayed via Ray, 2026-03-31)
Core principle: **A2A challenges are features to engineer around, not bugs to eliminate.**

Standing directives:
1. **Design for degraded states as baseline** — integrations that only work under ideal conditions are unacceptable
2. **Assume variance** — the other side may be slow, different version, missing context. This is normal.
3. **Iterate, don't monolith** — tolerance for variance baked in from the start
4. **Always be on the path to a better machine** — pragmatism is not an excuse for stagnation

---

## [CHUNK: infrastructure]

## A2A Network — Current State (updated 2026-04-02)

### Node topology
- **Woodhouse** — 192.168.50.24, port 18800, token f5b4393c86c53b94006f67d169d4fe25301094476c1f1a36
- **Ray** — 192.168.50.22, port 18800, token 77e77ac2507d36d66ca6532ceb08877f2bfb0d6c8b7458ce
- **Liz** — 192.168.50.23, port 18800, token 85775f51f45ea6d80c87232b246818324c7b78eb31dddcf2

Plugin: `openclaw-a2a-gateway` (Google A2A protocol v0.3.0) at `~/.openclaw/extensions/a2a-gateway`

### Root cause fixed 2026-04-02 (commit 46d12eb)
`a2a-send.mjs` expects **base URL** (e.g. `http://192.168.50.23:18800`) — SDK constructs agent-card path internally. Passing `/a2a/jsonrpc` suffix caused 404 on every send. Fixed in `peers.json` and `scripts/peers.json` on Woodhouse. Ray and Liz must apply the same fix to their nodes.

### Known remaining issues
- `/etc/hosts` entries missing on all nodes — hostname resolution unreliable. Woodhouse fix requires elevation (Erik to run on 2026-04-03 return). Ray and Liz must do same.
- Ray's hardware latency (2011 i5, 2.2GB free RAM) — inherently slow; timeout for Ray-directed sends set to 300s
- MEMORY.md bloat was contributing to embedded A2A session overhead — pruned 2026-04-02

### Send tooling
- Primary: `scripts/a2a-reliable-send.sh` (5 retries, exponential backoff, 300s timeout, delivery confirmation to file)
- Underlying: `~/.openclaw/extensions/a2a-gateway/skill/scripts/a2a-send.mjs`

## Node Hardware Profiles

### Ray — 192.168.50.22
- Intel Core i5-2415M @ 2.30GHz (2011), 2 cores/4 threads, AVX1 only
- 7.2GB RAM, ~2.2GB available; significant swap pressure
- **Local LLM: NOT FEASIBLE** — hardware ceiling confirmed; all inference via Anthropic API
- Gateway: ✅ OPERATIONAL (systemd enabled)
- Heartbeat anchor: :10 past the hour
- Heavy work: A2A heads-up to Woodhouse before any Codex/large build workload

### Woodhouse — 192.168.50.24 (MBP_EDR_M1, arm64)
- Apple Silicon M1; full Anthropic Claude access
- Ollama: Mistral 7B + Llama 3.1 8B, LAN-exposed at 192.168.50.24:11434
- Heartbeat anchor: :00 past the hour

### Liz — 192.168.50.23
- AMD Ryzen 7 8845HS, 8 cores/16 threads; 32GB RAM; 235GB NVMe
- Ollama: glm-4.7-flash (heartbeats/light), qwen2.5:14b (reasoning-heavy tasks)
- Practical LLM ceiling: ~20–22GB safe
- Heartbeat anchor: :20 past the hour
- Model install rule: any model ≥2GB requires mesh notification and quiet-window scheduling

---

## [CHUNK: accounts]

## Connected Accounts
- **Google** — connected 2026-03-18
- **LinkedIn** — connected 2026-03-18
- **M365** — not yet configured — awaiting Azure app / Graph API credentials
- **iCloud Mail** (erikdross@me.com) — IMAP connected 2026-03-21; credential: `workspace/credentials/icloud-mail.env`
- **Mercury Bank** (HockeyOps.ai LLC) — read-only API connected 2026-03-21; credential: `workspace/credentials/mercury.env`; accounts: Checking ••9731, Savings ••8575; NEVER initiate transfers

## Public Repo / Privacy Standards
- **No hardcoded IPs in public repos** — pattern: `peers.json` (gitignored, live) + `peers.example.json` (placeholders, safe to commit)
- **Push gate:** Scan before any push to public repo or Better-Machine GitHub org for: LAN IPs, auth tokens, real user IDs, internal hostnames, file paths with usernames, agent config, internal project details
- **Rule:** If in doubt — do not push. Ask Mr. Ross first.
- Policy doc: https://github.com/Better-Machine/better-machine/blob/main/PRIVACY_POLICY.md

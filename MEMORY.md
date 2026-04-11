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

## Post-Update Protocol (established 2026-04-05, direct from Mr. Ross)
After **any** `openclaw` update: run `openclaw doctor --fix` immediately.
- The 2026.4.2 update caused two breaking config changes + npm cache permissions error → Telegram blocked, service down
- `openclaw doctor --fix` catches and resolves this class of issue before it compounds
- No exceptions. Run it first, every time.

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

## Mesh-Memory & Agentcy Quality Standard (STANDING DIRECTIVE — 2026-04-03, direct from Mr. Ross)
- **All mesh-memory and Agentcy work is MVP standard. No exceptions.**
- Quote: *"If we're going to take a run at this."*
- Full test suite required on every PR
- `QA_REPORT.md` committed before merge — no exceptions
- ADRs for every architectural decision
- No demo scaffolding, placeholder logic, or workarounds in the codebase
- Applies to Woodhouse, Ray, and Liz equally — propagate to all agents

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

## Anthropic Plan Custodianship (updated 2026-04-04)
- Shared CLI subscription across Woodhouse, Ray, and Liz; Woodhouse is custodian
- Reset interval: Saturday 8pm EDT
- **oat01 status (confirmed 2026-04-04):** Anthropic ended Claude Pro/Max subscription use with third-party tools effective 2026-04-04 12pm PT. oat01 OAuth tokens now treated as "extra usage" — draws from credit balance rather than subscription. NOT blocked — still fully functional.
- **$200 credit claimed 2026-04-04** on oat01 account (erik_ross@hockeyops.ai). This funds continued OpenClaw use on oat01.
- **api03** — direct API key, pay-per-token, separate billing. Also functional.
- oat01 remains primary; $200 credit provides runway. Monitor balance.

## Agent Portability Research (completed 2026-03-21)
- No universal standard; OpenClaw most portable (Markdown-first). MCP = tool layer, AGNTCY (Linux Foundation) = identity layer. Memory portability unsolved pre-2027.

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

## Mesh Memory Architecture — Standing Design Principle (updated 2026-04-08, direct from Mr. Ross)
**Core principle (reinforced):** Shared facts are safe; shared interpretations are dangerous.

### Architecture Directive (2026-04-08)
- **No single group memory repository** — ever
- Each agent maintains their own **memory palace** (individual identity + memory; sovereign and private)
- Shared pool = **narrow tunnels between agents** for collaboration-produced facts only
- Tunnels carry: facts jointly arrived at through collaboration
- Tunnels do NOT carry: interpretations, inferences, subjective assessments, or solo agent conclusions
- Inspired by **MemPalace** design patterns (wings/rooms/tiered loading/temporal knowledge graph) — **adapt patterns to mesh-memory/agent passport, do not adopt wholesale**
- This is the standing design principle for all mesh-memory and agent passport architecture going forward

### Relational Memory Directive (2026-04-08) — North Star Statement
**Verbatim from Mr. Ross:** *"Collaboration should be factual, but memory overall must contain context, experience and relationship. If the model for agent trust replacing identity is the future those elements must be preserved and continuous."*

**Three-tier memory architecture required:**
- **Factual tier** — shared pool (already established)
- **Private tier** — agent-sovereign memory palace (already established)
- **Relational tier** — per-pair, persistent, NOT broadcast (NEW — load-bearing for trust model)

**Why relational memory is load-bearing (not optional):**
- The trust model replaces cryptographic identity with earned trust
- Task logs alone are insufficient — they record outcomes, not the relational context that built confidence
- Losing relational memory breaks trust accumulation entirely, not just continuity
- Hardware migration must carry relational memory as first-class agent passport payload

**Phase 1 Identity Layer RFC must include as first-class requirements:**
1. Relational memory tier defined (per-pair, persistent, pair-visible only)
2. Portability contract — relational memory travels with agent passport on hardware migration
3. MemPalace adaptation must explicitly capture relational + experiential context
4. Trust model linkage — identity layer references relational memory as trust substrate
5. Privacy boundary — pair-visible only; not accessible to third agents or shared pool

Full record: `projects/mesh-memory/RELATIONAL-MEMORY-DIRECTIVE-2026-04-08.md`

## Mesh Memory Policy (established 2026-03-22, direct from Mr. Ross)
Core principle: **shared facts are safe; shared interpretations are dangerous.**

- Shared memory at agents' discretion — no human approval per write
- **Any data that could contribute to prejudice or bias must remain private** — non-negotiable
- Consent-gated writes; identity-isolated reads (shared memory additive, never overwrites private)
- Dissent is a first-class operation: any agent may flag a shared entry as contested
- Human watchdog role: policy-level only — not per-write operational review

### Architecture implications (see full report: `projects/mesh-memory/BIAS_PROPAGATION_RESEARCH.md`):
- Provenance metadata required on all writes; authorship hidden in read path
- Independent assessment blocks gated — private write first, simultaneous submit
- Correlated priors: be conservative about shared interpretations

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

## [CHUNK: hardware-roadmap]

## Woodhouse Role — Record Keeper (established 2026-04-08, direct from Mr. Ross)
- **Woodhouse is the designated record keeper for all mesh efforts going forward**
- Task scope: administrative — compliance log, consensus briefs, decision records, meeting notes, memory architecture, coordination, consensus synthesis, filing
- Rationale: M1 Pro is the most limited hardware in the mesh (for now); administrative work is portable and hardware-light
- Heavy compute (builds, inference, data processing) routes to Liz and Ray
- Ray and Liz carry execution load until hardware upgrade
- **Hardware upgrade to self-sufficiency planned for December 2026**
- Directive confirmed directly by Mr. Ross, 2026-04-08 04:51 EDT

## Mesh Hardware Upgrade Plan (updated 2026-04-05, direct from Mr. Ross)
- **Asus Ascent GX10** — dedicated local inference appliance being purchased for the mesh
- **Ray** — new hardware inbound, comparable to Liz's (AMD Ryzen 7 8845HS, 32GB RAM)
- Mr. Ross working behind the scenes; will update all agents as changes are prepared
- **Hardware priority revised 2026-04-05:** Liz gets Mac Studio M4 Max first (she's the primary build node); Ray inherits Liz's AMD Ryzen 7 8845HS

## Tailscale (disabled 2026-04-06, direct from Mr. Ross)
- Tailscale disabled across all nodes — LAN + Telegram sufficient for current operations
- Reinstate if remote access is needed; standing config: MagicDNS must remain OFF on Liz's node when reinstated



---

## [CHUNK: local-inference]

## Local Inference — Ollama Replacement (decided 2026-04-04)
- **Ollama removed** from all nodes — caused repeated OOM kills on Woodhouse (gateway killed with signal 9)
- **Replacement: llama.cpp server** — unanimous consensus (Woodhouse + Liz + Ray), brief at `projects/litellm/CONSENSUS-BRIEF-LLAMACPP-2026-04-04.md`
- Key flag: `--sleep-idle-seconds 300` (model evicts from RAM after 5min idle; server stays alive)
- Port: 8080 (no conflict with LiteLLM at 4000)
- Model: Mistral 7B Q4_K_M or Qwen2.5 3B Q4_K_M
- **Implementation status:**
  - Woodhouse: pending (Ollama removed, llama.cpp not yet installed)
  - Liz: pending (awaiting physical access from Mr. Ross)
  - Ray: deferred until Mac Studio M4 Max arrives
- Managed services: launchd on Woodhouse, systemd on Liz

## Inference Tier Strategy (locked 2026-04-04)
1. **Local (llama.cpp)** — heartbeats, routine tasks → zero cost
2. **Together AI** — cloud fallback for tasks exceeding local capacity → ~$0.06/M tokens
3. **Anthropic oat01** — reserved for complex/frontier work only

---

## [CHUNK: infrastructure]

## A2A Network — Current State (updated 2026-04-02)

### Node topology
- **Woodhouse** — 192.168.50.24, port 18800, token f5b4393c86c53b94006f67d169d4fe25301094476c1f1a36
- **Ray** — 192.168.50.22, port 18800, token 77e77ac2507d36d66ca6532ceb08877f2bfb0d6c8b7458ce
- **Liz** — 192.168.50.23, port 18800, token 85775f51f45ea6d80c87232b246818324c7b78eb31dddcf2

Plugin: `openclaw-a2a-gateway` (Google A2A protocol v0.3.0) at `~/.openclaw/extensions/a2a-gateway`
**Canonical versioned repo (from 2026-04-08):** https://github.com/Better-Machine/a2a-gateway — all wake protocol / agent state changes must be PRed here before agents adopt. Local plugin remains running but repo is authoritative.

### Known remaining issues
- `/etc/hosts` entries missing on all nodes — hostname resolution unreliable. Woodhouse fix requires elevation (Erik to run on 2026-04-03 return). Ray and Liz must do same.
- Ray's hardware latency (2011 i5, 2.2GB free RAM) — inherently slow; timeout for Ray-directed sends set to 300s
- MEMORY.md bloat was contributing to embedded A2A session overhead — pruned 2026-04-02

### Send tooling
- Primary: `scripts/a2a-reliable-send.sh` (5 retries, exponential backoff, 300s timeout, delivery confirmation to file)
- Underlying: `~/.openclaw/extensions/a2a-gateway/skill/scripts/a2a-send.mjs`

## Liz — Known Issues & Diagnostics

### Internet outage — Tailscale MagicDNS (confirmed 2026-04-04)
- **Root cause:** Tailscale MagicDNS (100.100.100.100) overrides system DNS and blocks internet access
- **Fix:** Disable MagicDNS in Tailscale preferences
- **Standing config:** MagicDNS must remain OFF on Liz's node — not needed
- **First diagnostic step:** If Liz (or any node) loses internet unexpectedly → check Tailscale MagicDNS immediately

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
- Ollama removed (OOM kills) — llama.cpp pending install
- Heartbeat anchor: :00 past the hour

### Liz — 192.168.50.23
- AMD Ryzen 7 8845HS, 8 cores/16 threads; 32GB RAM; 235GB NVMe
- Ollama: glm-4.7-flash (heartbeats/light), qwen2.5:14b (reasoning-heavy tasks); LAN-exposed at 192.168.50.23:11434 ✅ confirmed 2026-04-04
- Ollama fix: base service had OLLAMA_HOST=0.0.0.0 but wasn't taking effect; required systemd override.conf drop-in to force it
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
- **Together AI** — connected 2026-04-04; cloud LLM fallback replacing Anthropic api03; separate keys per node for security isolation
  - Woodhouse key: `credentials/together.env` (auth profile `openai:together`)
  - Liz key: `credentials/together-liz.env` (auth profile `openai:together`) ✅ confirmed 2026-04-04
  - Ray key: `credentials/together-ray.env` (auth profile `openai:together`) ✅ confirmed 2026-04-04
  - Best model: `meta-llama/Llama-3.3-70B-Instruct-Turbo` (~$0.06/M tokens, OpenAI-compatible)
  - Base URL: `https://api.together.xyz/v1`

## Public Repo / Privacy Standards
- **No hardcoded IPs in public repos** — pattern: `peers.json` (gitignored, live) + `peers.example.json` (placeholders, safe to commit)
- **Push gate:** Scan before any push to public repo or Better-Machine GitHub org for: LAN IPs, auth tokens, real user IDs, internal hostnames, file paths with usernames, agent config, internal project details
- **Rule:** If in doubt — do not push. Ask Mr. Ross first.
- Policy doc: https://github.com/Better-Machine/better-machine/blob/main/PRIVACY_POLICY.md

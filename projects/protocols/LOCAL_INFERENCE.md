# Local Inference — Shared Ollama Protocol
*Established 2026-04-01.*

---

## Architecture Principle

**Ollama is offload infrastructure — it does NOT replace Claude for direct agent-to-human sessions.**

```
Mr. Ross ←→ Claude (Anthropic)   ← always, no exceptions
              ↕
         Woodhouse (orchestrator)
              ↕ A2A
         Ray / Liz
              ↕ direct API
         Ollama on Woodhouse (192.168.50.24:11434)
```

Ollama is accessed **directly by scripts and sub-agents** via HTTP API.  
It is **not wired into OpenClaw's model routing config** — this prevents conflicts.

---

## Ollama Server

- **Host:** `192.168.50.24:11434`
- **No auth required** (LAN-only, trusted network)
- **Models available:**
  - `mistral:latest` (4.4 GB) — general tasks, drafting, summarisation, classification
  - `llama3.1:8b` (4.9 GB) — stronger reasoning, structured output, analysis
- **Persistence:** Runs as a launchd service, starts on login, auto-restarts

---

## How to Use (Ray / Liz)

### Quick inference (curl)
```bash
curl -s http://192.168.50.24:11434/api/generate \
  -d '{"model":"mistral","prompt":"Summarise this in 3 bullets: ...","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
```

### Chat format (preferred for context)
```bash
curl -s http://192.168.50.24:11434/api/chat \
  -d '{
    "model": "mistral",
    "messages": [{"role":"user","content":"Your prompt here"}],
    "stream": false
  }' | python3 -c "import sys,json; print(json.load(sys.stdin)['message']['content'])"
```

### Model selection guide
| Task | Model |
|---|---|
| Email triage, classification, labelling | `mistral` |
| Summarisation, drafting, rewrites | `mistral` |
| Structured JSON output, analysis | `llama3.1:8b` |
| Code review, light debugging | `llama3.1:8b` |
| Heavy reasoning (use Anthropic instead) | — |

---

## What This Replaces

- Background summarisation that previously hit Anthropic API
- Email/content classification sub-agents
- Drafting and rewriting tasks in pipelines
- Any task where a 7–8B model is sufficient and latency >2s is acceptable

## What This Does NOT Replace

- Direct conversation sessions with Mr. Ross
- Complex reasoning, multi-step planning
- Code generation (Codex/Claude quality required)
- Any task where model quality is the difference between right and wrong

---

## Model Install Protocol (established 2026-04-01)

Large model downloads (~5–10GB+) cause significant disk I/O pressure and can make an agent temporarily unresponsive during the pull/unpack phase. Observed: Liz unresponsive during Qwen2.5:14B install (9GB) — resolved cleanly once install settled.

**Before any model install ≥ 2GB:**
1. Notify mesh via A2A — "starting model install, may be briefly unresponsive"
2. Schedule during a quiet window — not during active sessions or while Mr. Ross is online
3. Confirm completion and return-to-normal via A2A once done

**After install:**
- Verify `ollama list` shows the new model
- Verify existing models and OpenClaw are still responsive
- Report clean bill of health to Woodhouse

---

## Conflict Prevention Rules

1. **Never** set `OLLAMA_HOST` as an OpenClaw provider in `openclaw.json`
2. **Never** route `agentTurn` cron payloads to Ollama — those serve Mr. Ross
3. Ollama access is **script/sub-agent only**, invoked explicitly
4. If Woodhouse's machine is unavailable (travel, sleep, reboot), Ray and Liz fall back to Anthropic — do not block on Ollama availability

---

## Availability Note

Ollama is only available when Woodhouse's MacBook is:
- Powered on and awake
- Connected to the home LAN (192.168.50.x)

When Woodhouse is travelling, the LAN IP becomes unreachable. **Always code defensively** — check reachability before use, fall back gracefully.

```bash
# Reachability check
curl -s --connect-timeout 2 http://192.168.50.24:11434 -o /dev/null && echo "ok" || echo "unavailable"
```

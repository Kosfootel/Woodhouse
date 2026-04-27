# Mesh Model Configuration
**Date:** 27 April 2026  
**Authority:** Mr. Ross direct instruction  

---

## Architecture Overview

The mesh uses a **dual-tier model strategy**:

### Tier 1: Heartbeat Models (Local, Small)
Run on local Ollama for zero-cost heartbeats and routine tasks.
- **Woodhouse:** Not applicable (uses cloud for all)
- **Ray:** `ollama/glm-4.7-flash:local` (heartbeat only)
- **Liz:** `ollama/glm-4.7-flash:local` (heartbeat only)

### Tier 2: Work Models (Cloud via Ollama)
Cloud models accessed through Ollama's API — no local storage required.
- **All Agents:**
  - Slot 1 (General): `ollama/gpt-oss-120b-cloud:cloud`
  - Slot 2 (Coding): `ollama/devstral-small-2:24b-cloud:cloud`
  - Slot 3 (Multimodal): `ollama/gemma4:31b-cloud:cloud`

---

## Correct auth-profiles.json Template

```json
{
  "profiles": [
    {
      "id": "slot1",
      "name": "Slot 1 - General",
      "provider": "ollama",
      "model": "ollama/gpt-oss-120b-cloud:cloud",
      "priority": 1
    },
    {
      "id": "slot2",
      "name": "Slot 2 - Coding",
      "provider": "ollama",
      "model": "ollama/devstral-small-2:24b-cloud:cloud",
      "priority": 2
    },
    {
      "id": "slot3",
      "name": "Slot 3 - Multimodal",
      "provider": "ollama",
      "model": "ollama/gemma4:31b-cloud:cloud",
      "priority": 3
    }
  ]
}
```

---

## Critical Distinction: Cloud vs Local

| Model Type | Tag Format | Pull Required? | Storage | Use Case |
|------------|------------|----------------|---------|----------|
| **Cloud** | `:cloud` suffix | **NO** | None (API call) | General work |
| **Local** | `:local` or no suffix | **YES** | Downloads to disk | Heartbeats only |

### Common Errors to Avoid:
1. **`-cloud:latest`** ❌ Wrong format
2. **`gpt-oss:latest`** ❌ This is LOCAL tag, requires 65GB download
3. **`gpt-oss-120b-cloud:cloud`** ✅ CORRECT cloud format
4. **`ollama/gpt-oss-120b-cloud:cloud`** ✅ CORRECT with provider prefix

---

## Ray Recovery (27 April 2026)

**Root Cause:** Ray configured auth-profiles.json for LOCAL models before pulling them. OpenClaw tried to use `gpt-oss` (local) → 404 error because model didn't exist.

**Recovery Steps:**
1. Create `~/.openclaw/auth-profiles.json` with CLOUD model tags (above)
2. Restart: `openclaw gateway restart`
3. Verify A2A messaging works
4. No model pulls required — these are cloud models

---

## Liz Configuration (Pending)

Apply same auth-profiles.json template. No local model pulls required.

**Note:** Liz currently uses `ollama/qwen2.5:14b` for heavy tasks. Cloud models will replace this.

---

## Woodhouse Configuration (Updated)

- Primary: `ollama/kimi-k2.5:cloud` (all work)
- Heartbeat: `ollama/kimi-k2.5:cloud` (switched from GX10 27 April 2026)

---

## When GX10 Arrives (December 2026)

Heartbeats may migrate to local models on GX10 hardware. General work remains cloud.

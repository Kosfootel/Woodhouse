# Model Reconfiguration Brief
**Date:** 2026-04-26  
**Status:** DRAFT - Pending Team Review  
**Author:** Woodhouse (synthesizing Mr. Ross direction)  
**Reviewers:** Ray, Liz, Woodhouse → Mr. Ross

---

## 1. Executive Summary

This brief documents a strategic model reconfiguration across the Agentcy.services mesh, driven by two primary directives from Mr. Ross:

1. **Eliminate Chinese-hosted models** from the production inference stack
2. **Expand capability coverage** (vision, image generation, specialized coding) while maintaining non-Chinese hosting compliance

---

## 2. Reasoning for Change

### 2.1 Current State (Pre-Change)

| Model | Origin | Role | Classification |
|-------|--------|------|---------------|
| Kimi-k2.5:cloud | 🇨🇳 Moonshot AI (Beijing) | Generalist, long-context reasoning, vision | **Chinese-hosted** |
| Qwen3.x variants | 🇨🇳 Alibaba (Hangzhou) | Coding, reasoning | **Chinese-hosted** |
| GLM-4.7 flash | 🇨🇳 Zhipu AI (Beijing) | Local heartbeats (Ray, Liz) | **Chinese-hosted** |
| DeepSeek V3.1 | 🇨🇳 DeepSeek (Hangzhou) | Heavy reasoning | **Chinese-hosted** |

### 2.2 Rationale for Non-Chinese Migration

**Strategic Considerations:**
- **Data sovereignty:** Mesh operations involve HockeyOps.ai business data, M365 integration, and personal correspondence
- **Compliance positioning:** Agentcy.services as "A2A infrastructure for agents, by agents" requires clear hosting provenance for enterprise adoption
- **Supply chain risk:** Eliminating single-country-of-origin dependency for critical inference paths

**Capability Rationale:**
- Kimi-k2.5 is a capable generalist (256K context, vision, agentic) but overlaps significantly with Nemotron Super 120B
- Specialized gaps exist: web browsing, image generation, software-engineering-optimized coding
- Nemotron Super 120B already covers multi-agent workflows (96.30% RULER 256K) — we need complements, not overlaps

---

## 3. Target State: Full Mesh Model Architecture

### 3.1 GX-10 Hardware (New Inference Hub)

| Model | Origin | Parameters | VRAM | Role |
|-------|--------|-----------|------|------|
| **Nemotron Super 120B** | 🇺🇸 NVIDIA (Santa Clara) | 12B active / 120B total | ~87GB | Primary local heavy inference, multi-agent, long-context |
| **Nemotron Nano 4B** | 🇺🇸 NVIDIA (Santa Clara) | 4B | ~8GB | Edge tasks, fast inference, heartbeat backup |
| **FLUX.2 Klein 4B** | 🇩🇪 Black Forest Labs (Germany) | 4B (DiT) | ~16-24GB | **Image generation** (native PyTorch/diffusers, not via Ollama) |

**Notes:**
- FLUX.2 Klein runs via `diffusers` + PyTorch directly on GX-10 (RTX 4090 24GB)
- Ollama image generation is macOS-only (Jan 2026); Linux support "coming soon"
- Expected performance: ~0.4 seconds/image at 4 steps on RTX 4090

### 3.2 Ollama Cloud Pro Tier (3 Concurrent Slots)

| Slot | Model | Origin | Purpose | Replaces |
|------|-------|--------|---------|----------|
| **1** | `gpt-oss:120b-cloud` | 🇺🇸 OpenAI (San Francisco) | Chat quality, web browsing, reasoning variety | **Kimi-k2.5** |
| **2** | `devstral-small-2:24b-cloud` | 🇫🇷 Mistral + All Hands | Software engineering agent workflows, codebase exploration, multi-file editing | *New capability* |
| **3** | *(open for testing)* | — | — | — |

**Slot 3 Discussion:**
- Original proposal: FLUX.2 Klein via Ollama (blocked: Linux not supported)
- Alternative: Gemma 4 27B for vision/multimodal (but this overlaps with Nemotron capabilities)
- **Recommendation:** Leave Slot 3 open for now; FLUX.2 is covered on GX-10 locally

### 3.3 Per-Agent Local/Heartbeat Models

| Agent | Current | Proposed | Notes |
|-------|---------|----------|-------|
| **Woodhouse** | None (Ollama removed, llama.cpp pending) | **llama.cpp** (Mistral 7B Q4 or Qwen2.5 3B Q4) | Pending M1 Pro install |
| **Ray** | GLM-4.7 flash (🇨🇳) | **⚠️ REQUIRES CONFIRMATION** | Intel i5-2415M (2011), 2.2GB RAM — may need Together AI fallback |
| **Liz** | GLM-4.7 flash (🇨🇳) | **⚠️ REQUIRES CONFIRMATION** | AMD Ryzen 7 8845HS / Mac Studio M4 Max (if arrived) |

---

## 4. Capability Comparison: Kimi-k2.5 vs. Replacements

| Capability | Kimi-k2.5 (Outgoing) | GPT-OSS 120B (Slot 1) | Devstral-Small-2 (Slot 2) | Nemotron Super (Local) |
|-----------|----------------------|----------------------|--------------------------|------------------------|
| **Chat quality (Arena-Hard)** | ~75 | **90.26** ✅ | N/A | 73.88 |
| **Long context (256K)** | ✅ Excellent | 128K (sufficient) | Moderate | **96.30% RULER** ✅ |
| **Web browsing** | ❌ | **Native** ✅ | N/A | ❌ |
| **Multi-agent workflows** | Good | Good | **Specialized for SE agents** ✅ | **Purpose-built** ✅ |
| **Vision (image understanding)** | ✅ | ❌ | ❌ | ❌ |
| **Image generation** | ❌ | ❌ | ❌ | ❌ |
| **SWE-Bench coding** | ~74% | ~78% | **~60-65% (agent-optimized)** | 60.47% |
| **Codebase exploration** | Generalist | Generalist | **Specialized** ✅ | Generalist |
| **Origin** | 🇨🇳 China | 🇺🇸 US ✅ | 🇫🇷 France + US ✅ | 🇺🇸 US ✅ |

**Net Capability Changes:**
- ✅ **Gained:** Web browsing, superior chat quality (+15 points Arena-Hard), specialized SE agent workflows, image generation (via FLUX.2)
- ❌ **Lost:** Vision/image understanding (analyzing photos, OCR from images)
- ⚠️ **Risk:** If vision is critical, must swap Slot 3 to Gemma 4 27B

---

## 5. Model Assignment Changes by Agent

### 5.1 Woodhouse (192.168.50.24, MBP M1)

| Category | Current | Target |
|----------|---------|--------|
| **Heavy inference** | Anthropic oat01 (primary) + Together AI fallback | Nemotron Super 120B via GX-10 (A2A routing), oat01 for frontier only |
| **Local inference** | None (Ollama removed due to OOM kills) | **llama.cpp server** (Mistral 7B or Qwen2.5 3B Q4_K_M) — pending install |
| **Ollama Cloud** | Kimi-k2.5 | **gpt-oss:120b-cloud** (Slot 1) |

### 5.2 Ray (192.168.50.22, Intel i5-2415M 2011)

| Category | Current | Target |
|----------|---------|--------|
| **Heartbeat/local** | GLM-4.7 flash via Ollama | **⚠️ VERIFY:** May be infeasible on 2.2GB RAM; Together AI fallback likely required |
| **Heavy inference** | Together AI (meta-llama/Llama-3.3-70B) | Nemotron Super 120B via GX-10 |
| **Ollama Cloud** | Unknown | To be assigned based on workload |

**Ray Hardware Constraint:** Intel i5-2415M (2011), AVX1 only, 2.2GB available RAM. Local LLM likely impossible; all inference via API/cloud.

### 5.3 Liz (192.168.50.23)

| Category | Current | Target |
|----------|---------|--------|
| **Heartbeat/local** | GLM-4.7 flash via Ollama (local on AMD) | **⚠️ VERIFY:** Continue local or migrate to GX-10 routing? |
| **Heavy inference** | Ollama local (Qwen2.5:14b, glm-4.7-flash) | Nemotron Super 120B via GX-10 |
| **Ollama Cloud** | Unknown | **devstral-small-2:24b-cloud** (Slot 2, coding) |
| **Hardware** | AMD Ryzen 7 8845HS / 32GB RAM | **⚠️ VERIFY:** Mac Studio M4 Max arrival status |

---

## 6. LM Studio / Subagent Spawning on GX-10

### 6.1 Current Status

**Ray reports:** Successfully configured and tested GX-10 in LM Studio mode with subagent spawning (standard subagents + Agency agents).

### 6.2 Ray's Verified LM Studio Configuration ✅

**Status:** OPERATIONAL — Subagent spawning tested and confirmed working

| Setting | Value |
|---------|-------|
| **Provider Name** | `gx10-lab` (custom local provider) |
| **Base URL** | `http://192.168.50.20:1234/v1` |
| **Models Available** | `nvidia/nemotron-3-super` (120B), `nvidia/nemotron-nano-4b` (4B) |
| **Authentication** | None (local network) |
| **Performance** | ~20 tokens/second on Super 120B (RTX 5090) |
| **OpenClaw Config** | `~/.openclaw/config/model-providers/gx10-lab.json` |

**Subagent Spawning Test Results:** ✅ CONFIRMED

```typescript
// Standard subagent
sessions_spawn({
  task: "Your task here...",
  runtime: "acp",
  model: "gx10-lab/nemotron-3-super",  // or nvidia/nemotron-nano-4b
  timeoutSeconds: 600
})
```

| Test | Model | Result |
|------|-------|--------|
| Nano 4B subagent | `nvidia/nemotron-nano-4b` | ✅ Completed task, generated response |
| Super 120B subagent | `nvidia/nemotron-3-super` | ✅ Completed task, generated response |

**Known Issue — Return Path:**
- **Problem:** Subagent completion announcements failing
- **Error:** `FailoverError: Unknown model: together/moonshotai/Kimi-K2.5`
- **Root Cause:** Announcement/fallback model references removed `together` provider
- **Impact:** Subagents EXECUTE correctly on GX-10, but completion announcements crash
- **Fix Required:** Update announcement/fallback model from `together/moonshotai/Kimi-K2.5` → `ollama/kimi-k2.5:cloud` or `gx10-lab/nemotron-nano-4b`

**Troubleshooting Notes:**

| Issue | Diagnosis | Status |
|-------|-----------|--------|
| SSH to GX-10 host fails | Process running but SSH not configured for Ray's user | Not needed — API access sufficient |
| Subagent announcements fail | Stale fallback model reference | Fix pending config update |
| Speed slower than expected | ~20 tok/s on 120B is normal for RTX 5090 | Within expected range |

**For Liz and Woodhouse Replication:**
- GX-10 provider config is stable
- Subagent spawning works (routing to GX-10 successful)
- Fix needed: Update announcement/fallback model
- Recommendation: Consider making GX-10 nano the fallback for subagent completions — eliminates external API dependency

---

### 6.4 Implementation Target

| Agent | Current Subagent Method | Target GX-10 Method | Status |
|-------|------------------------|---------------------|--------|
| Woodhouse | Anthropic oat01 (local) | GX-10 LM Studio (Nemotron Super 120B) | ⏳ Pending replication |
| Ray | Together AI (cloud) | GX-10 LM Studio | ✅ **OPERATIONAL** |
| Liz | Ollama local (AMD) | GX-10 LM Studio | ⏳ Pending replication |

---

## 7. Implementation Checklist

### Phase 1: Verification (Team)
- [x] Ray confirms: GLM-4.7 flash heartbeat status, Ollama Cloud assignments — **DONE**
- [x] Ray documents: GX-10 LM Studio configuration for replication — **DONE**
- [ ] Liz confirms: Current hardware (AMD vs Mac Studio), heartbeat model status, Ollama Cloud assignments
- [ ] Woodhouse confirms: llama.cpp install plan for M1 Pro

### Phase 2: Ollama Cloud Reconfiguration
- [ ] Mr. Ross approves brief
- [ ] Swap Slot 1: Kimi-k2.5 → gpt-oss:120b-cloud
- [ ] Assign Slot 2: devstral-small-2:24b-cloud
- [ ] Decide Slot 3: Leave open vs Gemma 4 27B (vision gap analysis)

### Phase 3: GX-10 FLUX.2 Installation
- [ ] Install `diffusers`, `torch`, `transformers` on GX-10
- [ ] Download FLUX.2 Klein 4B (Apache 2.0) from HuggingFace
- [ ] Verify sub-1-second generation on RTX 4090
- [ ] Document API/wrapper for agent access

### Phase 4: LM Studio Rollout
- [x] Ray validates GX-10 LM Studio setup — **DONE**
- [ ] Liz replicates Ray's GX-10 LM Studio setup
- [ ] Woodhouse replicates GX-10 LM Studio setup
- [ ] Test cross-agent subagent spawning via GX-10
- [ ] Fix announcement/fallback model configuration
- [ ] Document fallback paths (Anthropic oat01 for Woodhouse, Together AI for Ray)

### Phase 5: Heartbeat Migration
- [ ] Evaluate GLM-4.7 flash replacement (if Chinese exclusion extends to heartbeats)
- [ ] Alternative: llama.cpp local models (if hardware permits)
- [ ] Alternative: Route heartbeats to GX-10 Nemotron Nano 4B

---

## 8. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| **Vision capability loss** (no image understanding) | High | Medium | Monitor; add Gemma 4 to Slot 3 if critical use case emerges |
| **Ray local inference impossible** | Certain | Low | Continue Together AI fallback; route heavy work to GX-10 |
| **FLUX.2 Linux setup complexity** | Medium | Low | Ray has proven path; document and replicate |
| **LM Studio instability** | Low | High | Maintain Anthropic/Together AI fallbacks |
| **Heartbeat model (GLM-4.7) remains Chinese** | Current | Low | Defer; heartbeats are low-sensitivity operational traffic |

---

## 9. Team Review Required

**Ray:** ✅ **CONFIRMED — See Section 6.2 for verified configuration**

**Liz:** Please confirm or correct:
1. Current hardware status (AMD Ryzen vs Mac Studio M4 Max)
2. Current heartbeat model(s) and Ollama Cloud assignments
3. Ability to replicate Ray's GX-10 LM Studio setup
4. Whether you need Woodhouse coordination on GX-10 access

**Liz:** Please confirm or correct:
1. Current hardware status (AMD Ryzen vs Mac Studio M4 Max)
2. Current heartbeat model(s) and Ollama Cloud assignments
3. Ability to replicate Ray's GX-10 LM Studio setup

**Woodhouse:** Will update brief based on team feedback, then submit to Mr. Ross for final review.

---

## 10. Appendix: Model Origins Reference

| Model | Developer | Origin | Classification |
|-------|-----------|--------|---------------|
| gpt-oss | OpenAI | 🇺🇸 San Francisco | US-hosted ✅ |
| devstral-small-2 | Mistral + All Hands | 🇫🇷 Paris + 🇺🇸 US | European/US ✅ |
| nemotron-3-super | NVIDIA | 🇺🇸 Santa Clara | US-hosted ✅ |
| flux2-klein | Black Forest Labs | 🇩🇪 Germany | European ✅ |
| gemma4 | Google | 🇺🇸 Mountain View | US-hosted ✅ |
| kimi-k2.5 | Moonshot AI | 🇨🇳 Beijing | **Chinese-hosted** ❌ |
| qwen3.x | Alibaba | 🇨🇳 Hangzhou | **Chinese-hosted** ❌ |
| glm-4.7 | Zhipu AI | 🇨🇳 Beijing | **Chinese-hosted** ❌ |
| deepseek | DeepSeek | 🇨🇳 Hangzhou | **Chinese-hosted** ❌ |

---

**End of Brief**

*Pending team verification and Mr. Ross approval.*

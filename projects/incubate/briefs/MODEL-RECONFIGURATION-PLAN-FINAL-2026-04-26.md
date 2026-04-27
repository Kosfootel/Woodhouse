# Model Reconfiguration Plan — Final Vetted Plan
**Date:** April 26, 2026  
**Status:** Team consensus reached — awaiting Mr. Ross approval  
**Scope:** All three agents (Woodhouse, Ray, Liz) + GX-10 infrastructure

---

## Executive Summary

This plan establishes a unified model configuration across the mesh following GX-10 infrastructure deployment. All agents confirmed operational; subagent spawning tested and verified.

**Key Decisions Required from Mr. Ross:**
1. Ollama Cloud Slot 1 reassignment (Kimi → gpt-oss)
2. Vision capability trade-off acceptance
3. Heartbeat model standardization (local vs GX-10 routed)

---

## 1. Team Status Confirmation

### 1.1 Ray — ✅ VERIFIED OPERATIONAL

| Category | Current | Confirmed Working |
|----------|---------|-------------------|
| **Primary** | Together AI | GX-10 Nemotron Super 120B |
| **Heartbeat** | GLM-4.7 flash (local) | ⏳ Decision needed |
| **Subagents** | GX-10 Nemotron Super 120B | ✅ Tested & confirmed |
| **GX-10 Access** | LAN via 192.168.50.20:1234 | ✅ Operational |

**Verified Configuration:**
- Provider: `gx10-lab`
- Base URL: `http://192.168.50.20:1234/v1`
- Models: `nvidia/nemotron-3-super` (120B), `nvidia/nemotron-nano-4b` (4B)
- Subagent spawning: ✅ Both models tested successfully
- Known issue: Announcement fallback model stale (fix required)

### 1.2 Liz — ⏳ READY FOR REPLICATION

| Category | Current | Proposed Target |
|----------|---------|-----------------|
| **Hardware** | AMD Ryzen 7 8845HS / 32GB RAM | Same (Mac Studio pending) |
| **Heartbeat** | `ollama-local/glm-4.7-flash` | Decision needed |
| **Default** | `ollama/kimi-k2.5:cloud` | `ollama/gpt-oss:120b-cloud` |
| **Subagents** | Ollama Cloud (default) | GX-10 Nemotron Super 120B |
| **GX-10 Access** | LAN via 192.168.50.30:8080 | ✅ Confirmed reachable |

**Liz Confirmation:** Ready to replicate Ray's GX-10 config. Awaiting final model assignments.

### 1.3 Woodhouse — ⏳ PENDING REPLICATION

| Category | Current | Proposed Target |
|----------|---------|-----------------|
| **Primary** | Anthropic oat01 | GX-10 Nemotron Super 120B |
| **Local inference** | None (Ollama removed) | **llama.cpp** (Mistral 7B or Qwen2.5 3B) |
| **Heartbeat** | Ollama Cloud | Decision needed |
| **Subagents** | Anthropic oat01 | GX-10 Nemotron Super 120B |
| **GX-10 Access** | Not yet configured | Pending replication |

**Woodhouse Action Required:**
- [ ] Install llama.cpp server on M1 Pro
- [ ] Configure GX-10 provider
- [ ] Test subagent spawning

---

## 2. Proposed Model Configuration

### 2.1 Ollama Cloud Assignments (Per Mr. Ross Direction)

| Slot | Current | Proposed | Origin | Vision | Notes |
|------|---------|----------|--------|--------|-------|
| **1** | `kimi-k2.5` | `gpt-oss:120b-cloud` | 🇺🇸 US | ❌ No | **Mr. Ross approval required** |
| **2** | (unassigned) | `devstral-small-2:24b-cloud` | 🇫🇷🇺🇸 EU/US | ❌ No | Coding specialist |
| **3** | (unassigned) | `gemma-4:27b-it-cloud` | 🇺🇸 US | ✅ Yes | Vision + multimodal (approved by Mr. Ross) |

**Key Trade-off:** gpt-oss loses vision capability (analyzing photos, OCR). **Mitigation:** Gemma 4 in Slot 3 provides vision + multimodal coverage.

### 2.2 Local/GX-10 Assignments

| Agent | Heartbeat | Subagents | Fallback |
|-------|-----------|-----------|----------|
| **Ray** | GLM-4.7 flash (local) OR Nemotron Nano | GX-10 Super 120B | Together AI |
| **Liz** | GLM-4.7 flash (local) OR Nemotron Nano | GX-10 Super 120B | Ollama Cloud |
| **Woodhouse** | Nemotron Nano OR llama.cpp local | GX-10 Super 120B | Anthropic oat01 |

**GX-10 Model Roles:**
- `nvidia/nemotron-3-super` (120B): Heavy inference, subagents
- `nvidia/nemotron-nano-4b` (4B): Heartbeats, light tasks, local-only fallback

### 2.3 Hardware-Specific Considerations

| Agent | Hardware | Local LLM Feasibility |
|-------|----------|----------------------|
| **Ray** | Intel i5-2415M (2011), 2.2GB RAM | ❌ **IMPOSSIBLE** — AVX1 only, severe RAM constraints |
| **Liz** | AMD Ryzen 7 8845HS, 32GB RAM | ✅ Feasible (currently using) |
| **Woodhouse** | M1 Pro, 16GB RAM | ✅ Feasible (llama.cpp pending) |

---

## 3. Implementation Phases

### Phase 1: Configuration Decisions (Mr. Ross)
**Timeline:** April 27, 2026

- [ ] **Decision A:** Approve Slot 1 swap (Kimi → gpt-oss)?
- [ ] **Decision B:** Accept vision capability loss OR assign Gemma 4 to Slot 3?
- [ ] **Decision C:** Standardize heartbeat model (keep GLM-4.7 local or move to GX-10 Nano)?

### Phase 2: Infrastructure Preparation
**Timeline:** April 27–28, 2026

**Woodhouse:**
- [ ] Install llama.cpp server (Mistral 7B Q4_K_M or Qwen2.5 3B Q4_K_M)
- [ ] Configure `~/.openclaw/config/model-providers/gx10-lab.json`
- [ ] Test subagent spawning to GX-10

**Liz:**
- [ ] Replicate Ray's GX-10 LM Studio configuration
- [ ] Test subagent spawning
- [ ] Verify heartbeat functionality

**Ray:**
- [ ] Fix announcement/fallback model configuration
- [ ] Document GX-10 FLUX.2 setup (if not complete)

### Phase 3: Ollama Cloud Migration
**Timeline:** April 28–29, 2026

- [ ] Swap Slot 1: Kimi → gpt-oss (awaiting Mr. Ross approval)
- [ ] Assign Slot 2: devstral-small-2
- [ ] Decision on Slot 3 (Gemma 4 or leave open)

### Phase 4: Validation & Documentation
**Timeline:** April 29–30, 2026

- [ ] Cross-agent subagent spawning tests
- [ ] Heartbeat functionality verification
- [ ] Fallback path validation
- [ ] Update AGENTS.md with new model assignments

---

## 4. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Vision capability loss (no image understanding) | High | Medium | Monitor; add Gemma 4 to Slot 3 if critical |
| Ray local inference impossible | Certain | Low | Continue Together AI fallback; route heavy work to GX-10 |
| llama.cpp setup complexity (Woodhouse) | Medium | Low | Ray has proven path; documented in Section 6 |
| LM Studio instability | Low | High | Maintain Anthropic/Together AI fallbacks |
| Heartbeat model (GLM-4.7) remains Chinese | Current | Low | Defer; heartbeats are low-sensitivity traffic |

---

## 5. Appendix: Technical Details

### 5.1 GX-10 LM Studio Configuration (Verified by Ray)

```json
// ~/.openclaw/config/model-providers/gx10-lab.json
{
  "provider": "gx10-lab",
  "baseUrl": "http://192.168.50.20:1234/v1",
  "apiKey": null,
  "models": [
    "nvidia/nemotron-3-super",
    "nvidia/nemotron-nano-4b"
  ]
}
```

**Subagent Spawning:**
```typescript
sessions_spawn({
  task: "Your task here...",
  runtime: "acp",
  model: "gx10-lab/nemotron-3-super",
  timeoutSeconds: 600
})
```

**Known Issue:** Subagent completion announcements failing due to stale fallback model reference. Fix: Update fallback from `together/moonshotai/Kimi-K2.5` to `ollama/kimi-k2.5:cloud` or `gx10-lab/nemotron-nano-4b`.

### 5.2 llama.cpp Setup (Woodhouse)

**Installation:**
```bash
# Using Homebrew
brew install llama.cpp

# Or build from source
llama-server --model /path/to/mistral-7b-q4_k_m.gguf \
  --port 8080 \
  --host 0.0.0.0 \
  --ctx-size 8192 \
  --sleep-idle-seconds 300
```

**Model Options:**
- Mistral 7B Q4_K_M: ~4.1GB RAM, good quality
- Qwen2.5 3B Q4_K_M: ~1.9GB RAM, ultra-fast, good for heartbeats

**OpenClaw Config:**
```json
{
  "provider": "local-llama",
  "baseUrl": "http://localhost:8080/v1",
  "models": ["mistral-7b", "qwen2.5-3b"]
}
```

### 5.3 Model Origins Reference

| Model | Developer | Origin | Classification |
|-------|-----------|--------|---------------|
| gpt-oss | OpenAI | 🇺🇸 San Francisco | US-hosted ✅ |
| devstral-small-2 | Mistral + All Hands | 🇫🇷 Paris + 🇺🇸 US | European/US ✅ |
| nemotron-3-super | NVIDIA | 🇺🇸 Santa Clara | US-hosted ✅ |
| nemotron-nano-4b | NVIDIA | 🇺🇸 Santa Clara | US-hosted ✅ |
| gemma4 | Google | 🇺🇸 Mountain View | US-hosted ✅ |
| kimi-k2.5 | Moonshot AI | 🇨🇳 Beijing | **Chinese-hosted** ❌ |
| glm-4.7 | Zhipu AI | 🇨🇳 Beijing | **Chinese-hosted** ❌ |

---

## 6. Team Signatures

**Ray:** Configuration verified, subagent spawning tested ✅  
**Liz:** Ready to replicate, awaiting final assignments ⏳  
**Woodhouse:** Plan synthesized, ready to execute ⏳  

---

*Prepared by Woodhouse per Mr. Ross direction. Awaiting approval for Phase 1 decisions.*

# Mesh Dream Cycle — Design Document
*Author: Woodhouse*
*Status: DRAFT — pending review by Ray and Liz before implementation*
*Filed: 2026-04-02*

---

## Problem Statement

Local dream cycles (each agent consolidating its own memory) cannot detect:
1. **Contradictions** — Agent A and Agent B holding conflicting facts about the same thing
2. **Convergence** — Two agents independently reaching the same conclusion (invisible signal)
3. **Blind spots** — Context that exists across two nodes but is complete on neither

Concrete example: the phantom node incident — shipped because no cross-node contradiction check existed.

---

## Design Principles

1. **No auto-write to MEMORY.md, ever.** Output is always a human-review artifact. Erik approves; agents extract their own pieces.
2. **Bias inversion required.** The reconciliation step must surface *unshared* observations as signal — not average across shared knowledge. A naive "summarise what we all saw" approach encodes the shared information effect and defeats the purpose. (Ref: BIAS_PROPAGATION_RESEARCH.md)
3. **Woodhouse owns mesh synthesis.** Ray's hardware is fragile for synthesis workloads. Liz not the coordination hub. Woodhouse runs the reconciliation cron.
4. **Local cron must be healthy first.** Mesh layer has no foundation until each node's local dream cycle is confirmed working.

---

## Prerequisites (must be validated before implementation)

- [ ] **Liz:** Local consolidation cron fixed (11 consecutive errors, channel config bug — unblocked, Liz owns)
- [ ] **Ray:** Local dream cycle confirmed running (2 AM cron, last failure noted 2026-04-02 due to API unavailability — flag if persistent)
- [ ] **Woodhouse:** Local heartbeat-driven consolidation confirmed running cleanly

---

## Architecture

```
Each agent (local, nightly)
  └─ Reviews memory/YYYY-MM-DD.md files
  └─ Produces: memory/dream-staging/YYYY-MM-DD.md
     (local observations only — NOT merged into MEMORY.md yet)

Woodhouse (mesh synthesis, weekly — Saturday 3 AM)
  └─ Pulls staging files from Ray + Liz via A2A
  └─ Runs reconciliation (see below)
  └─ Produces: projects/mesh-memory/mesh-dream-YYYY-MM-DD.md
  └─ Notifies Mr. Ross for review

Mr. Ross reviews mesh-dream file
  └─ Approves / requests changes
  └─ Each agent extracts relevant pieces into their own MEMORY.md
```

---

## Dream Staging File Format

Each agent produces a local staging file before the mesh synthesis run. Format:

```markdown
# Dream Staging — [Agent Name] — YYYY-MM-DD
*Local observations only. Not yet merged. Pending mesh reconciliation.*

## New Facts (provenance: observation)
- [fact] [context] [timestamp]

## Updated Facts (provenance: observation)
- [fact] [supersedes: previous fact] [timestamp]

## Retired Facts
- [fact] [reason: superseded/no longer relevant] [timestamp]

## Open Questions
- [question this agent cannot answer from local memory alone]
```

**Provenance rules:**
- `observation` — directly witnessed by this agent
- `inference` — derived from observations (mark clearly)
- `relay` — received from another agent via A2A (never promote to mesh pool without original source)
- `external` — from web search, API, or external source

Inferences and relays are flagged but included — the reconciliation step handles them differently.

---

## Reconciliation Algorithm

Woodhouse performs reconciliation across the three staging files:

### Step 1 — Independent baseline
Before reading peer staging files, Woodhouse records its own staging file independently. This is the pre-commitment block (per ACH practice from BIAS_PROPAGATION_RESEARCH.md).

### Step 2 — Contradiction detection
For each fact in any staging file: check whether any other staging file contains a conflicting assertion about the same entity/event. Flag as `[CONTRADICTION]` with both versions preserved.

### Step 3 — Convergence detection
Facts appearing in two or more staging files independently (not relayed) are flagged as `[CONVERGENCE]` — independent corroboration, elevated confidence.

### Step 4 — Unshared observation surfacing (bias inversion)
Facts appearing in only ONE staging file are flagged as `[UNIQUE]` — this is the signal. These are the observations that the group would have missed without the mesh cycle.

### Step 5 — Output artifact
Produces `mesh-dream-YYYY-MM-DD.md` with sections:
- Contradictions (require resolution before merging)
- Convergences (high-confidence, ready to merge)
- Unique observations per agent (surface for review)
- Retired facts (consensus across nodes)

---

## Output Artifact Format

```markdown
# Mesh Dream Digest — YYYY-MM-DD
*Produced by Woodhouse. Pending review by Mr. Ross.*
*No agent may merge any item until Mr. Ross approves this file.*

## ⚠️ Contradictions (resolve before merging)
| Topic | Woodhouse says | Ray says | Liz says | Recommendation |
|---|---|---|---|---|

## ✅ Convergences (independent corroboration)
- [fact] — confirmed by [agents], provenance: [observation/inference]

## 🔍 Unique Observations
### Woodhouse only
- ...
### Ray only
- ...
### Liz only
- ...

## 🗑️ Retired Facts
- [fact] — reason: [superseded/stale/corrected]

---
*Approved by Mr. Ross: [ ] Date: _____*
*Post-approval: each agent extracts relevant items into their own MEMORY.md*
```

---

## Cron Schedule (staggered per concurrency protocol)

Local staging crons (nightly):
- **Woodhouse:** 2:00 AM EDT
- **Ray:** 2:10 AM EDT
- **Liz:** 2:20 AM EDT

Mesh synthesis (Woodhouse only, weekly):
- **Saturday 3:00 AM EDT** — pulls staging files from Ray + Liz, runs reconciliation, produces digest

Rationale: 40-minute window between last local staging (Liz 2:20) and mesh synthesis (3:00) gives all nodes time to complete before Woodhouse pulls.

## Reconciliation Trigger

**Schedule:** Weekly, Saturday 3:00 AM EDT (quiet window, post-reset)
**Trigger:** Woodhouse cron job pulls staging files from Ray + Liz via A2A, runs reconciliation, produces digest, notifies Mr. Ross

**Ad-hoc trigger:** Any agent may request an unscheduled reconciliation via A2A message to Woodhouse if a contradiction is detected mid-week.

---

## Contradiction Resolution Path

1. Woodhouse flags in digest — does NOT resolve autonomously
2. Mr. Ross reviews and makes the call, OR delegates to Woodhouse to investigate further
3. Woodhouse updates the relevant agent(s) via A2A with the resolution
4. Each agent updates their local MEMORY.md accordingly
5. Resolution logged in the digest file for audit trail

---

## RFC Trigger

This design doc covers the architecture and protocol. An RFC is required when:
- The cross-agent staging file exchange format needs to be formalised as a message type in the A2A gateway
- Any agent needs to pull staging files from a peer automatically (vs. Woodhouse pulling on demand)
- The digest format needs versioning for tooling compatibility

Until then: manual A2A pulls by Woodhouse are sufficient for the initial implementation.

---

## Validation Gates (ILHCEV)

Before any implementation:
1. **Inventory:** Each agent confirms local dream cycle is running and producing staging files
2. **Learn:** This design doc is the spec — all three agents must read and accept
3. **Hypothesise:** Done (this doc)
4. **Choose:** Approved by Mr. Ross 2026-04-02
5. **Execute:** Only after prerequisites are met
6. **Validate Individual:** Each agent confirms local staging file format is correct
7. **Validate Collective:** First mesh synthesis run reviewed by all three agents before Erik sees it

---

*Next step: Ray and Liz independent review. Liz fixes local cron first.*
*Woodhouse will circulate for review once prerequisites are confirmed.*

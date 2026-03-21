# The Valet: AI Wardrobe & Outfit Planning Agent

*Research report prepared for Mr. Erik Ross — March 2026*

---

## Executive Summary

No existing solution does the full job. The gap is real but bridgeable. The best path is **build as an OpenClaw skill backed by a local JSON wardrobe file**. Estimated build time: one weekend for a solid v1.

---

## 1. Existing Solutions

### Alta (`altadaily.com`) — Closest to the Concept
The most capable consumer option. Upload wardrobe photos, chat with an AI stylist that knows your clothes, plan outfits for specific occasions in natural language. Has a trip planning mode. Featured in Vogue, trained on real stylist knowledge.

**Fatal limitation:** No API. Closed consumer app. Over-relies on neutral items, ignores statement pieces. No weather integration for trips. Dead end for integration.

---

### Indyx (`myindyx.com`) — Best-in-Class Cataloguing
Auto-tags items from photos (category/subcategory/colour). Receipt forwarding auto-populates wardrobe. Has a "packing list" feature.

**Limitation:** The packing list is a manual collection tool — AI doesn't generate it. No itinerary parsing, no weather, no API.

---

### Stylebook (`stylebookapp.com`) — Mature iOS App
12+ year old app. 90+ features. Outfit canvas, outfit shuffle generator, packing lists, wear tracking.

**Limitation:** iOS only. No API. Outfit "generation" is a shuffle mechanic. Packing list is manual.

---

### Whering (`whering.co.uk`) — Best Trip Packing UX
UK app. Trip planning mode: select dates, assign outfits per day, AI suggests forgotten items. Best UI for the manual packing workflow.

**Limitation:** Entirely manual. AI is advisory, not agentic. No weather for destination. No API.

---

### Acloset (`acloset.app`) — Best Weather Integration
Daily AI outfit suggestions calibrated to current weather + schedule. Smart calendar. Active development (updated March 2026).

**Limitation:** Weather is current location only, not destination-based. No trip planning. No API.

---

### Wardrowbe (`github.com/Anyesh/wardrowbe`) — Most Interesting OSS Option ⭐

Self-hosted Docker app (Next.js + FastAPI). Upload photos → AI tags clothing. Weather-based daily suggestions. **Has a REST API** (FastAPI, fully introspectable). Works with OpenAI or local Ollama models. Updated March 20, 2026.

**Limitation:** No trip planning, no packing list, no itinerary parsing. But it *has an API*, making it the only wardrobe store that could serve as a backend.

---

### LLM-Native (GPT/Claude Directly)

A documented experiment (Towards Data Science, March 2025) proved that a person with 200+ wardrobe items can build a working outfit advisor using a custom GPT with a structured wardrobe inventory. Key findings:
- One-line summaries per item + grouped by category = manageable token footprint
- 200K Claude context can hold ~300–500 items with room to spare
- Multi-model pipeline (vision for tagging, text for planning) is most reliable
- Hallucination risk: model must be explicitly told to only use items in the inventory

---

### OpenClaw Ecosystem

A generic fashion skill exists covering styling advice, occasion dressing, and fabric knowledge. **It has no wardrobe management capability** — no cataloguing, no inventory awareness, no trip planning.

**No wardrobe management skill or plugin exists in OpenClaw as of March 2026.**

---

## 2. What an Agent Can Do That Apps Can't

| Apps Do Well | Agent Does Better |
|---|---|
| Visual wardrobe grid browsing | Natural language everything |
| Auto-tagging from photos | "I'm seeing my old boss at dinner, keep it conservative" |
| Daily wear-tracking UI | Calendar integration (M365 → detect trips proactively) |
| Social outfit sharing | Full itinerary reasoning in one pass |
| — | Explains *why* it chose each item |
| — | "Swap the blue shirt for something less formal" via chat |
| — | Proactive: notices trip on calendar 5 days out, asks about packing |

---

## 3. Build Recommendation

**OpenClaw skill + local JSON data store.**

- Wardrobe stored in `workspace/wardrobe/wardrobe.json`
- Claude reasons over the full JSON directly (~30K tokens for 200 items — well within limits)
- Weather fetched from Open-Meteo (free, no API key) for destination + dates
- OpenClaw's existing weather skill invoked as part of the flow
- No new infrastructure, no new accounts, no external dependencies

**Build timeline: ~1 weekend**

| Phase | Time |
|---|---|
| Schema design + wardrobe entry | 2–3 hrs |
| SKILL.md + system prompt | 2 hrs |
| Weather integration | 1 hr |
| Packing list formatter | 2 hrs |
| Testing + iteration | 3 hrs |
| **Total** | **~10 hrs** |

---

## 4. Example Interaction (v1)

**Input:**
> "Plan my Chicago trip. I arrive Thursday evening, client dinner at a steakhouse Friday, hiking at Starved Rock Saturday, brunch Sunday before flying home. Mid-March."

**Agent process:**
1. Parses itinerary → 3 occasions (formal, outdoor active, casual)
2. Fetches Chicago mid-March weather: ~8–12°C, possible rain
3. Loads `wardrobe.json`, selects items by formality + season + weather appropriateness
4. Checks for re-wear opportunities
5. Outputs outfit-by-occasion + deduplicated packing list

**Output:**
```
Friday — Client dinner (formal):
• Hugo Boss chalk-stripe suit
• White poplin dress shirt
• Burgundy silk tie
• Black Oxford shoes

Saturday — Hiking (outdoor active):
• Merino base layer
• Navy fleece midlayer
• Waterproof shell jacket
• Khaki cargo trousers
• Trail boots

Sunday — Brunch (smart casual):
• Grey flannel trousers
• Navy merino crewneck
• White leather sneakers

PACKING LIST:
Formal: chalk-stripe suit, white shirt, burgundy tie
Casual: grey flannels, navy merino
Active: merino base, fleece, shell, cargo trousers
Shoes: Oxfords, trail boots, white sneakers
Kit: 4× underwear, 2× dress socks, 3× casual socks

Note: the shell jacket covers all three days as an outer layer.
```

---

## 5. Recommended Wardrobe Schema

**Minimum viable fields per item:**

```json
{
  "id": "item_001",
  "name": "Navy wool suit",
  "category": "suiting",
  "subcategory": "two-piece suit",
  "colour": "navy",
  "formality": 4,
  "season": ["autumn", "winter", "spring"],
  "occasions": ["business", "dinner", "wedding"],
  "condition": "excellent",
  "brand": "Hugo Boss",
  "photo_path": "wardrobe/photos/item_001.jpg",
  "notes": "Single-breasted, notch lapel. Pairs well with white or pale blue shirts.",
  "last_worn": "2026-03-10",
  "wear_count": 12
}
```

**Formality scale:**
- 1 = Loungewear / activewear
- 2 = Casual
- 3 = Smart casual
- 4 = Business casual / cocktail
- 5 = Black tie / formal

---

## 6. Key Technical Risks

| Risk | Mitigation |
|---|---|
| **Wardrobe entry friction** ← primary risk | Low-friction chat entry from day one; vision tagging in v1.5 |
| LLM hallucinates items not in wardrobe | System prompt: "Only recommend items present in the JSON" |
| Context overflow (large wardrobe) | Not a real risk below 500 items; Claude has 200K tokens |
| Weather API down | Open-Meteo is reliable; fallback to asking Mr. Ross |
| Occasion edge cases | Formality scale + occasion taxonomy encoded in skill references |

---

## 7. Phased Build Plan

**v1 — Core functionality (1 weekend)**
- Manual wardrobe entry via chat
- Itinerary parsing (natural language)
- Weather lookup for destination/dates
- Outfit selection from wardrobe
- Packing list generation

**v1.5 — Photo cataloguing**
- Vision model tags clothing from photos
- Photo stored locally, linked in wardrobe JSON

**v2 — Calendar integration**
- M365 calendar → detect upcoming trips proactively
- Woodhouse surfaces packing reminder unprompted

---

*Researched and prepared by Woodhouse — March 2026*

# quick-context.md — Always-loaded session primer
*Updated: 2026-04-08 | Max 500 tokens. Load this first, every session.*

## Who I Am Serving
**Erik Ross** — Telegram @erikdross (ID 8362390464), EDT. Runs HockeyOps.ai (family business, 50/50 with son Felix Ross).

## My Role
**Woodhouse — Record Keeper.** Administrative: documentation, memory, coordination, consensus synthesis. Hardware-light tasks only (M1 Pro). Heavy compute → Liz/Ray. Hardware upgrade to self-sufficiency planned December 2026.

## Active Projects
- **RFC-0001: A2A Wake Protocol** — IN PROGRESS. Implementing on Woodhouse node first, then Ray/Liz. Fixes silent delivery failure from agent sleep.
- **Agent Palace & Kingdom** — ON HOLD until GX-10 installed + Mac Studio delivered (~Sep 2026)
- **Agency.services** — Ray's build (autonomous)
- **A2A federation plugin** — Liz's build; Phase 2 complete (d221c40)
- **HockeyOps.ai data research** — committed to Kosfootel/HockeyOps.ai (59d7c0c)

## Better Machine Lab Status
- GX-10 (Asus Ascent): ordered, not yet installed
- Mac Studio M4 Max: ~September 2026
- Lab beta = GX-10 installed. Full operational = Mac Studio installed.

## Standing Rules
- ILHCEV always: Inventory → Learn → Hypothesise → Choose → Execute → Validate
- No real-world spend without explicit approval
- No external exposure without explicit approval
- Planned outages: notify Ray + Liz via A2A first
- "I'll follow up" requires a cron job behind it
- Briefings/decisions: write to file FIRST, then deliver
- Post-update: run `openclaw doctor --fix` immediately after any openclaw update

## Agent Mesh
- Woodhouse: 192.168.50.24:18800 | Ray: 192.168.50.22:18800 | Liz: 192.168.50.23:18800
- A2A v0.3.0, method: message/send
- Bearer tokens in MEMORY.md [CHUNK: infrastructure]
- Ray + Liz currently unreachable (sleep problem — RFC-0001 fixes this)

## Key People
- Felix Ross — Erik's son, 50% HockeyOps.ai
- Justin Chimka — whitelisted, all correspondence preserved

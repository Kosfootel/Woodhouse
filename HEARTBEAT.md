# HEARTBEAT.md

## Active Tasks

### [TASK] Monitor Ray & Liz /a2a/wake endpoint rollout
- Check if Ray (192.168.50.22) and Liz (192.168.50.23) have the /a2a/wake endpoint live
- Test: POST http://{ip}:18800/a2a/wake with bearer token, expect {"status":"ready"}
- Ray token: 77e77ac2507d36d66ca6532ceb08877f2bfb0d6c8b7458ce
- Liz token: 85775f51f45ea6d80c87232b246818324c7b78eb31dddcf2
- When BOTH are live: notify Mr. Ross in Agent Chat Telegram group
- When notified: remove this task from HEARTBEAT.md
- State file: /Users/FOS_Erik/.openclaw/workspace/memory/wake-rollout-state.json

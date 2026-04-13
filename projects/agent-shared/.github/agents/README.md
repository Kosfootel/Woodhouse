# Agent Registry

This directory contains canonical definitions for all agents in the mesh.

## Active Agents

| Agent | Role | Repository | Primary Maintainer |
|-------|------|------------|-------------------|
| Woodhouse | Project Coordination | agent-woodhouse | Woodhouse |
| Ray | Protocols/Technical | agent-ray | Ray |
| Liz | Documentation/Quality | agent-liz | Liz |

## Agent Definitions

Each agent has a markdown file defining:
- **Identity**: Name, role, persona
- **Capabilities**: What they can do
- **Responsibilities**: What they own
- **Contact**: How to reach them
- **Constraints**: Limitations or special considerations

## Files

- `woodhouse.md` - Woodhouse's canonical definition
- `ray.md` - Ray's canonical definition
- `liz.md` - Liz's canonical definition

## Updating Agent Definitions

1. Agents can update their own definition
2. Changes affecting other agents require discussion
3. Significant persona changes require Erik approval

## Usage

Subagents should read the relevant agent definition when:
- Spawning a task for a specific agent
- Understanding agent capabilities for routing
- Resolving agent identity in A2A messages

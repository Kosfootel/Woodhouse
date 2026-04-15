# Agent Testing Tools — Team Documentation

**Date:** 2026-04-14  
**Prepared by:** Woodhouse  
**For:** Liz, Ray, and Woodhouse

---

## Overview

We now have two agent testing frameworks installed:

1. **Agent Harness** — Primary tool for testing agency agents
2. **Inspect** — Secondary tool for model evaluation

Both are configured to use our GX-10 server (192.168.50.30) for local inference.

---

## Quick Start

### Agent Harness

```bash
# List available benchmarks
harness benchmarks

# Run a simple test
harness run \
    --agent agents/simple_qa_agent.py \
    --benchmark arithmetic \
    --num-tasks 10

# View results
harness view ./results/arithmetic
```

### Inspect

```bash
# Run an evaluation
inspect eval my_task.py --model gx10/nemotron-super-120b:local

# View logs
inspect view
```

---

## GX-10 Model Endpoints

All tools are pre-configured to use GX-10:

| Model | Endpoint | Use Case |
|-------|----------|----------|
| Nemotron Super (120B) | 192.168.50.30:8080 | Complex reasoning |
| Nemotron Nano (4B) | 192.168.50.30:8081 | Quick tasks |
| Nomic Embed | 192.168.50.30:8082 | Embeddings |

**No API keys required** — GX-10 is on our local network.

---

## Agent Harness: Deep Dive

### Why Agent Harness?

- **Language-agnostic:** Test agents in any language (Python, Rust, Go, etc.)
- **JSON-RPC protocol:** Standardized communication
- **Built-in benchmarks:** GAIA, Terminal-Bench, ARC-AGI
- **Crash recovery:** Resume interrupted runs
- **Metrics tracking:** Steps, tool usage, latency

### Writing an Agent for Harness

```python
from harness.agent import Agent
from harness.providers.base import Message

class MyAgent(Agent):
    def run_task(self, task_id: str, task_data: dict) -> str:
        # Track custom metrics
        self.increment("steps")
        
        # Your agent logic
        response = self.complete([
            Message(role="user", content=task_data["question"])
        ])
        
        self.record_tool_use("llm_call")
        return response.message.content

if __name__ == "__main__":
    MyAgent().run()
```

### Running Against Benchmarks

```bash
# GAIA (general assistant tasks)
harness run --agent my_agent.py --benchmark gaia-level1

# Terminal-Bench (DevOps tasks in Docker)
harness run \
    --agent agents/terminal_agent.py \
    --benchmark terminal-bench \
    --difficulty easy

# Arithmetic (simple math for testing)
harness run --agent my_agent.py --benchmark arithmetic
```

### Continuing Failed Runs

```bash
# Resume where you left off
harness continue <run-id>
```

---

## Custom Benchmarks for Better Machine

Woodhouse has designed benchmarks specifically for our A2A mesh:

### 1. A2A Coordination (P0)
- Message passing reliability
- Wake protocol testing  
- State synchronization
- Timeout handling

### 2. Memory Operations (P0)
- Read/write consistency
- Cross-agent memory sharing
- Semantic search accuracy

### 3. Research Workflows (P1)
- Multi-source synthesis
- Fact validation
- Source attribution

### 4. Multi-Agent Consensus (P1)
- Three-agent agreement
- Dissent handling
- Convergence time

**Full specifications:** See `research/agent-testing-deep/benchmarks/BENCHMARK-DESIGN.md`

---

## Configuration Files

All configs are in `~/.openclaw/workspace/agent-testing-config/`:

- `agent-harness-config.yaml` — Agent Harness settings
- `inspect-models.yaml` — Inspect model definitions
- `sample-test.py` — Example agent implementation

---

## Common Commands

### Agent Harness

```bash
# Install (already done)
pip install agent-eval-harness

# List benchmarks
harness benchmarks

# Run single task
harness run-one \
    --agent ./agent.py \
    --task '{"id": "test", "data": {"question": "What is 2+2?"}}'

# Run with custom model
harness run \
    --agent my_agent.py \
    --benchmark gaia-level1 \
    --model nemotron-super-120b

# Continue interrupted run
harness continue <run-id>

# View results
harness view ./results/gaia-level1/<run-id>
```

### Inspect

```bash
# Install (already done)
pip install inspect-ai

# Run evaluation
inspect eval my_task.py --model gx10/nemotron-super-120b:local

# View logs
inspect view

# List available models
inspect list models
```

---

## When to Use Which

| Use Case | Recommended Tool |
|----------|------------------|
| Test agency agents on multi-step tasks | **Agent Harness** |
| Benchmark against GAIA/ARC-AGI | **Agent Harness** |
| Terminal/DevOps tasks (Docker) | **Agent Harness** |
| Model comparison (which LLM is better) | **Inspect** |
| Academic evaluation | **Inspect** |
| ReAct agent scaffolding | **Inspect** |

---

## Troubleshooting

### "Connection refused" to GX-10
- Verify GX-10 is powered on
- Check endpoints: `curl http://192.168.50.30:8080/v1/models`
- Contact Woodhouse or Ray for GX-10 status

### Agent Harness can't find agent
- Ensure agent file is executable: `chmod +x agent.py`
- Check agent implements `run_task` method
- Verify JSON-RPC protocol is correct

### Out of memory on GX-10
- Use Nemotron Nano (4B) instead of Super (120B)
- Reduce `max_tokens` parameter
- Check `nvidia-smi` on GX-10 for GPU memory

---

## Resources

- **Agent Harness docs:** README in `research/agent-testing-deep/agent-harness/repo/`
- **Inspect docs:** https://inspect.aisi.org.uk/
- **Benchmark designs:** `research/agent-testing-deep/benchmarks/BENCHMARK-DESIGN.md`
- **Integration guide:** `research/agent-testing-deep/integration/INTEGRATION-ANALYSIS.md`

---

## Next Steps

1. **Familiarize:** Try running the sample test agent
2. **Experiment:** Run GAIA level 1 against your agent
3. **Custom benchmarks:** Implement A2A coordination tests
4. **CI/CD:** Integrate into PR checks

Questions? Ask Woodhouse.

---

*Tools installed and configured by Woodhouse, 2026-04-14*

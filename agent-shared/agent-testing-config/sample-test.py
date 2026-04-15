#!/usr/bin/env python3
"""
Sample Agent Harness test for Better Machine
Tests basic connectivity to GX-10 endpoints
"""

from harness.agent import Agent
from harness.providers.base import Message

class SimpleTestAgent(Agent):
    def run_task(self, task_id: str, task_data: dict) -> str:
        # Track metrics
        self.increment("steps")
        
        # Simple completion call to test GX-10 connectivity
        response = self.complete([
            Message(role="user", content=task_data.get("question", "Say hello"))
        ])
        
        self.record_tool_use("llm_call")
        return response.message.content

if __name__ == "__main__":
    SimpleTestAgent().run()

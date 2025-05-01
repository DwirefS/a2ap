"""
LangChain Adapter for A2AP

This adapter allows a LangChain agent (e.g., LLM chain or tool agent) to send
and receive structured A2AP messages using the Envelope + Payload schema.

It wraps around LangChain's LLM or chain object and exposes a `send` method
that builds a proper A2APMessage and returns a structured simulated response.

Usage Example:
    from langchain.llms import OpenAI
    from langchain_adapter import A2AChain

    llm = OpenAI(temperature=0.3)
    agent = A2AChain(llm=llm, metadata={"agent_id": "agent://doc-bot"})
    response = agent.send(goal="Summarize this document", receiver="agent://summarizer")
"""

from datetime import datetime
import uuid
from typing import Any, Dict

from protocol import Envelope, Payload, Goal, Context, Action, A2APMessage


class A2AChain:
    def __init__(self, llm: Any, metadata: Dict[str, str]):
        """
        Initialize A2AChain adapter with an LLM and agent metadata.

        Args:
            llm: A LangChain-compatible LLM object.
            metadata: Dictionary including 'agent_id' and optionally 'session_id', etc.
        """
        self.llm = llm
        self.agent_id = metadata.get("agent_id", "agent://unknown")
        self.metadata = metadata

    def send(self, goal: str, receiver: str, context_metadata: Dict[str, str] = None) -> Dict:
        """
        Constructs an A2AP message and simulates sending it to another agent.

        Args:
            goal (str): The task or objective the agent should complete.
            receiver (str): Target agent URI.
            context_metadata (Dict): Optional metadata such as originating tool or session.

        Returns:
            Dict: Simulated response structure including message payload and status.
        """
        # Construct goal
        goal_obj = Goal(
            description=goal,
            priority="medium",
            deadline=(datetime.utcnow().replace(microsecond=0).isoformat() + "Z")
        )

        # Create context
        context = Context(
            session_id=str(uuid.uuid4()),
            metadata=context_metadata or {"origin": "langchain_adapter"}
        )

        # Action being sent to receiver agent
        action = Action(
            type="QUERY",
            params={"prompt": goal}
        )

        # Full A2AP payload
        payload = Payload(goal=goal_obj, context=context, action=action)

        # Envelope with simulated token and signature
        envelope = Envelope(
            sender_id=self.agent_id,
            receiver_id=receiver,
            auth_token="mock-jwt-token",
            signature="mock-signature-sha256"
        )

        message = A2APMessage(envelope=envelope, payload=payload)

        # In a real scenario, you’d dispatch message over network here
        # For simulation, we generate a mock LLM response
        print("\n📤 A2AP Message Sent:")
        print(message.json(indent=2))

        simulated_llm_result = self.llm.predict(goal)

        return {
            "receiver": receiver,
            "original_goal": goal,
            "response": simulated_llm_result,
            "status": "success (simulated)",
            "timestamp": datetime.utcnow().isoformat()
        }

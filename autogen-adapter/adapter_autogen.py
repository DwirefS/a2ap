"""
AutoGen Adapter for A2AP

This module wraps a basic AutoGen-compatible agent to construct and respond
to messages using the A2AP protocol schema. This enables AutoGen-based tools
to receive structured agent messages, parse them, and act accordingly.

NOTE: This is a minimal implementation for compatibility. Integration with
a full AutoGen pipeline would involve callbacks and async handling.

"""

from datetime import datetime
import uuid
from typing import Dict, Optional
from protocol import Envelope, Payload, Goal, Context, Action, A2APMessage


class AutoGenA2AAdapter:
    def __init__(self, agent_id: str = "agent://autogen"):
        """
        Initialize the adapter with a default agent identifier.
        """
        self.agent_id = agent_id

    def receive_message(self, message: A2APMessage) -> Dict:
        """
        Simulates receiving an A2AP message and producing a structured response.

        Args:
            message (A2APMessage): The incoming message from another agent.

        Returns:
            Dict: Structured response with debug context.
        """
        print("\n📥 Received A2AP Message:")
        print(message.json(indent=2))

        action_type = message.payload.action.type
        response = {
            "status": "received",
            "action": action_type,
            "agent_id": self.agent_id,
            "original_goal": message.payload.goal.description,
            "response_time": datetime.utcnow().isoformat()
        }

        # Optional: hook into real AutoGen pipeline here

        return response

    def build_response_message(self, receiver: str, session_metadata: Optional[Dict] = None) -> A2APMessage:
        """
        Build a simulated response A2APMessage for testing.

        Args:
            receiver (str): The agent to respond to.
            session_metadata (dict): Optional metadata.

        Returns:
            A2APMessage: Message to be returned or sent.
        """
        goal = Goal(description="Acknowledge receipt", priority="low", deadline="2025-06-01T00:00:00Z")
        context = Context(session_id=str(uuid.uuid4()), metadata=session_metadata or {})
        action = Action(type="NOTIFY", params={"message": "AutoGen adapter received your message."})
        payload = Payload(goal=goal, context=context, action=action)
        envelope = Envelope(sender_id=self.agent_id, receiver_id=receiver)
        return A2APMessage(envelope=envelope, payload=payload)

"""
A2AP Simulator CLI Tool

This script simulates the generation and sending of a message from one agent to another
using the A2AP protocol defined in protocol.py. It constructs an Envelope and Payload,
validates them via Pydantic, and prints the message as a JSON object.

Usage:
$ python simulator.py
"""

import uuid
from datetime import datetime
import json
from protocol import Envelope, Payload, Goal, Context, Action, A2APMessage


def generate_message(sender_id: str, receiver_id: str) -> A2APMessage:
    """Constructs and returns a full A2APMessage"""

    goal = Goal(
        description="Turn off hallway lights if no motion detected",
        priority="high",
        deadline=(datetime.utcnow().replace(microsecond=0).isoformat() + "Z")
    )

    context = Context(
        session_id=str(uuid.uuid4()),
        metadata={
            "sensor_status": "idle",
            "location": "hallway",
            "origin": "motion-sensor-001"
        }
    )

    action = Action(
        type="EXECUTE",
        params={
            "device": "hallway-light",
            "command": "power_off"
        }
    )

    payload = Payload(
        goal=goal,
        context=context,
        action=action
    )

    envelope = Envelope(
        sender_id=sender_id,
        receiver_id=receiver_id,
        auth_token="mock-jwt-token-xyz",
        signature="mock-signature-sha256"
    )

    message = A2APMessage(envelope=envelope, payload=payload)
    return message


def main():
    """Main entry point for the CLI simulator"""
    print("\n🔄 Simulating A2AP Agent-to-Agent Message Exchange...")
    sender = "agent://motion-controller"
    receiver = "agent://light-controller"

    message = generate_message(sender, receiver)

    print("\n✅ Generated A2AP Message (JSON):\n")
    print(message.json(indent=2))


if __name__ == "__main__":
    main()

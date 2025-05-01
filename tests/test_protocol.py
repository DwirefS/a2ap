"""
Unit Tests for A2AP Protocol Models

These tests validate the correct construction and validation behavior
of the Envelope, Goal, Context, Action, Payload, and A2APMessage classes.
"""

import pytest
from protocol import Envelope, Goal, Context, Action, Payload, A2APMessage
from datetime import datetime


def test_envelope_creation():
    envelope = Envelope(
        sender_id="agent://source-agent",
        receiver_id="agent://target-agent",
        auth_token="test-token",
        signature="abc123signature"
    )
    assert envelope.sender_id == "agent://source-agent"
    assert "T" in envelope.timestamp  # ISO8601 format check


def test_goal_validation_pass():
    goal = Goal(
        description="Shutdown idle compute node",
        priority="high",
        deadline="2025-05-01T12:00:00Z"
    )
    assert goal.priority == "high"
    assert "T" in goal.deadline


def test_goal_validation_fail():
    with pytest.raises(ValueError):
        Goal(description="Invalid goal", priority="urgent", deadline="invalid-date")


def test_payload_construction():
    goal = Goal(description="Test action", priority="medium", deadline="2025-06-01T10:00:00Z")
    context = Context(session_id="xyz001", metadata={"requestor": "tester"})
    action = Action(type="EXECUTE", params={"key": "value"})
    payload = Payload(goal=goal, context=context, action=action)
    assert isinstance(payload, Payload)
    assert payload.action.type == "EXECUTE"


def test_full_message_creation():
    goal = Goal(description="Execute diagnostic", priority="low", deadline="2025-07-01T09:00:00Z")
    context = Context(session_id="abc456", metadata={"tool": "test-runner"})
    action = Action(type="NOTIFY", params={"message": "Ping received"})
    payload = Payload(goal=goal, context=context, action=action)
    envelope = Envelope(sender_id="agent://pingbot", receiver_id="agent://logger")
    message = A2APMessage(envelope=envelope, payload=payload)

    assert isinstance(message.payload, Payload)
    assert message.envelope.sender_id.startswith("agent://")

from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Literal
from datetime import datetime
import uuid

# Envelope structure
class Envelope(BaseModel):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    sender_id: str
    receiver_id: str
    auth_token: Optional[str] = None
    signature: Optional[str] = None

    @validator('timestamp')
    def validate_timestamp_format(cls, v):
        try:
            datetime.fromisoformat(v.replace('Z', '+00:00'))
            return v
        except ValueError:
            raise ValueError("Timestamp must be ISO8601 format")

# Goal definition
class Goal(BaseModel):
    description: str
    priority: Literal["low", "medium", "high"]
    deadline: str

    @validator('deadline')
    def validate_deadline_format(cls, v):
        try:
            datetime.fromisoformat(v.replace('Z', '+00:00'))
            return v
        except ValueError:
            raise ValueError("Deadline must be ISO8601 format")

# Context data
class Context(BaseModel):
    session_id: Optional[str]
    metadata: Dict[str, Optional[str]]

# Action to be executed by receiving agent
class Action(BaseModel):
    type: Literal["QUERY", "EXECUTE", "NEGOTIATE", "NOTIFY"]
    params: Dict[str, str]

# Complete payload
class Payload(BaseModel):
    goal: Goal
    context: Context
    action: Action

# Combined message object
class A2APMessage(BaseModel):
    envelope: Envelope
    payload: Payload

# Example usage (for testing)
if __name__ == "__main__":
    goal = Goal(description="Adjust lighting", priority="high", deadline="2025-06-01T10:00:00Z")
    context = Context(session_id="sess001", metadata={"origin": "user-request"})
    action = Action(type="EXECUTE", params={"device": "lamp", "state": "on"})
    payload = Payload(goal=goal, context=context, action=action)
    envelope = Envelope(sender_id="agent://room-controller", receiver_id="agent://smart-lamp")
    message = A2APMessage(envelope=envelope, payload=payload)

    print(message.json(indent=2))

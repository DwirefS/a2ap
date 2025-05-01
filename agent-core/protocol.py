from pydantic import BaseModel
class Envelope(BaseModel):
    message_id: str
    timestamp: str
    sender_id: str
    receiver_id: str
    auth_token: str
    signature: str

class Goal(BaseModel):
    description: str
    priority: str
    deadline: str

class Context(BaseModel):
    session_id: str
    metadata: dict

class Action(BaseModel):
    type: str
    params: dict

class Payload(BaseModel):
    goal: Goal
    context: Context
    action: Action
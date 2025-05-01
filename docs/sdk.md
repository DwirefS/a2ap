# A2AP SDK – Developer Documentation

## Overview
This SDK enables LLM agents, IoT devices, or microservices to interact using the A2AP protocol — which includes a secure Envelope + Payload schema, adapters, and transport abstractions.

---

## 📦 Installation

```bash
pip install a2ap
```

---

## 📂 SDK Structure

```
a2ap/
├── agent-core/             # Core protocol logic and schema definitions
├── langchain-adapter/      # LangChain agent wrapper
├── autogen-adapter/        # AutoGen integration hook
├── cli-tools/              # Simulation tools and diagnostics
├── examples/               # Reference use cases
└── tests/                  # Unit + integration tests
```

---

## 🔐 Message Schema Example

```python
from agent_core.protocol import Envelope, Payload, Goal, Context, Action

goal = Goal(description='Turn off lights', priority='high', deadline='2025-05-01T22:00:00Z')
context = Context(session_id='abc123', metadata={'user': 'admin'})
action = Action(type='EXECUTE', params={'device': 'lights', 'state': 'off'})
payload = Payload(goal=goal, context=context, action=action)

envelope = Envelope(
    message_id='uuid-001',
    timestamp='2025-05-01T21:45:00Z',
    sender_id='agent://control',
    receiver_id='agent://iot-light',
    auth_token='signed-jwt',
    signature='hash'
)
```

---

## 🧠 LangChain Integration

```python
from langchain_adapter.adapter import A2AChain

agent = A2AChain(llm=my_llm, metadata={"agent_id": "agent://docbot"})
response = agent.send(goal="Summarize document", receiver="agent://summarizer")
print(response["status"])
```

---

## 🛠 CLI Simulator

```bash
python cli-tools/simulator.py
```

Simulates sending structured A2AP messages between two agents using test data.

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## ✅ Adapter Status

| Adapter         | Status    | SDK Path              |
|-----------------|-----------|------------------------|
| LangChain       | ✔️ Ready  | langchain-adapter/     |
| AutoGen         | 🔧 In Dev | autogen-adapter/       |
| Custom REST API | 🧪 Planned | http-adapter/ (future) |

---

## 🌐 Upcoming Features

- Message queue transport (Kafka/MQTT/libp2p)
- Agent registry integration
- CLI-based message debugger
- WebSocket real-time channel for live simulation

---

## 🤝 Contribute

This SDK is open-source. Review [`CONTRIBUTING.md`](../CONTRIBUTING.md) for how to submit enhancements, adapters, or bug fixes.


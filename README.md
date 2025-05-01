# 🤖 A2AP – Agent-to-Agent Communication Protocol

![License](https://img.shields.io/github/license/DwirefS/a2ap)
![Built With Python](https://img.shields.io/badge/built%20with-python-blue)
![Status](https://img.shields.io/badge/status-v0.1--alpha-orange)
![Open Source](https://img.shields.io/badge/community-driven-brightgreen)

---

## 🧠 What is A2AP?

**A2AP (Agent-to-Agent Protocol)** is a secure, extensible, and interoperable communication protocol that allows autonomous agents — including LLMs, APIs, IoT devices, and robotic systems — to exchange structured messages with each other.

Built with a clean Envelope + Payload schema, A2AP enables cross-platform agent orchestration using a unified language of goals, context, and actions.

---

## ❓ Why A2AP?

Despite rapid growth in multi-agent systems, there's no modern, open standard for secure and interoperable agent messaging:

- LangChain, AutoGen, and other frameworks lack a shared agent communication protocol
- FIPA/KQML are outdated or overly academic
- Proprietary agent frameworks don’t scale across ecosystems

**A2AP fills the gap** by offering:
- 🚀 Developer-first SDKs
- 🔐 Built-in security (mTLS, JWT, RBAC, ZKP-ready)
- 🧱 Adapter support for LangChain, AutoGen, REST, MQTT

---

## 🧩 Architecture Overview

```
LangChain Agent --> A2AChain Adapter --> Envelope+Payload --> gRPC --> AutoGen Adapter --> AutoGen Agent
                                           ↘ Logger/CLI ↙            ↘ Agent Registry ↙
```

📷 [See full architecture diagram](architecture.md)  
📄 [See protocol spec (RFC)](A2AP-RFC-v0.1.md)

---

## ✨ Core Features

- **📦 Envelope + Payload schema** using Pydantic
- **🧠 LangChain & AutoGen Adapters** (LLM/Tool integration)
- **📡 Transport agnostic**: HTTP/gRPC/MQTT/libp2p
- **🔧 CLI Simulator** to test A2A messaging locally
- **📜 Open RFC governance model**

---

## 💻 Installation

```bash
pip install -r requirements.txt
```

Requires Python 3.10+

---

## 🚀 Quick Start

```python
from langchain.llms import OpenAI
from langchain_adapter import A2AChain

agent = A2AChain(llm=OpenAI(), metadata={"agent_id": "agent://docbot"})
response = agent.send(goal="Summarize this PDF", receiver="agent://summarizer")
print(response)
```

Run a full simulation:
```bash
python demo_agent.py
```

---

## 📁 Project Structure

```
/agent-core/             -> Envelope + Payload schema (Pydantic)
/langchain-adapter/      -> LangChain integration
/autogen-adapter/        -> AutoGen message handler
/cli-tools/              -> CLI simulator
/examples/               -> Sample agent scripts
/tests/                  -> Pytest test cases
/docs/                   -> RFC, SDK, Pitch, Diagrams
```

---

## 🔌 Integrations

| Framework    | Status     | Notes                            |
|--------------|------------|----------------------------------|
| LangChain    | ✅ Ready   | via `A2AChain`                   |
| AutoGen      | ✅ Ready   | via `AutoGenA2AAdapter`          |
| REST/MQTT    | 🚧 Planned | v0.2 roadmap                     |

---

## 🌐 Community

- 🤝 [Contributing Guidelines](CONTRIBUTING.md)
- 🛡 [Code of Conduct](CODE_OF_CONDUCT.md)
- 💬 GitHub Discussions (coming soon)
- 🧠 A2A-OSS Working Group (Q3 2025)

---

## 🗺 Roadmap

| Milestone               | Status     |
|------------------------|------------|
| RFC Draft v0.1         | ✅ Complete |
| SDK Alpha              | ⏳ In Dev   |
| Task Coordination Layer| 🚧 v0.2     |
| Ontology Negotiation   | 🧪 v0.3     |
| v1.0 Stable             | 📌 Q1 2026  |

---

## 🧾 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- LangChain
- OpenAI
- AutoGen by Microsoft
- Contributors across GitHub

Together, we’re building the next generation of intelligent, cooperative agents.


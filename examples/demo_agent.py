"""
Demo A2AP Agent

This example agent uses the A2AChain (LangChain adapter) to construct and send
a message to a simulated receiver agent, and optionally uses AutoGenA2AAdapter
to respond to a follow-up message. It demonstrates full-circle A2AP messaging.

Run this to simulate one round of goal-driven communication.
"""

from langchain.llms import OpenAI
from langchain_adapter import A2AChain
from autogen_adapter import AutoGenA2AAdapter
from protocol import A2APMessage

def run_demo():
    print("\n🚀 Starting A2AP Agent Demo...")
    
    # Step 1: Initialize the LangChain-based sender
    mock_llm = OpenAI(temperature=0.1)  # Replace with actual LLM credentials if needed
    doc_agent = A2AChain(llm=mock_llm, metadata={"agent_id": "agent://doc-bot"})

    # Step 2: Simulate sending a goal to another agent
    receiver_id = "agent://summary-agent"
    goal_description = "Summarize the attached medical report."
    response = doc_agent.send(goal=goal_description, receiver=receiver_id)

    print("\n📬 LangChain Agent Response:")
    print(response)

    # Step 3: Receive that message with AutoGen and build a response
    print("\n📨 Simulating receipt by AutoGen-based agent...")
    autogen_agent = AutoGenA2AAdapter(agent_id=receiver_id)

    # Simulate receiving the message back
    message_obj = A2APMessage.parse_obj({
        "envelope": {
            "message_id": "demo-001",
            "timestamp": "2025-05-01T14:00:00Z",
            "sender_id": "agent://doc-bot",
            "receiver_id": receiver_id,
            "auth_token": "token-1234",
            "signature": "sig-xyz123"
        },
        "payload": {
            "goal": {
                "description": goal_description,
                "priority": "medium",
                "deadline": "2025-05-01T15:00:00Z"
            },
            "context": {
                "session_id": "sess-demo-001",
                "metadata": {
                    "origin": "langchain_adapter"
                }
            },
            "action": {
                "type": "QUERY",
                "params": {
                    "prompt": goal_description
                }
            }
        }
    })

    receiver_response = autogen_agent.receive_message(message_obj)
    print("\n📨 AutoGen Agent Simulated Response:")
    print(receiver_response)


if __name__ == "__main__":
    run_demo()

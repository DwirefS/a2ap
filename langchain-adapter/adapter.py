class A2AChain:
    def __init__(self, llm, metadata):
        self.llm = llm
        self.metadata = metadata
    def send(self, goal, receiver):
        return {
            "receiver": receiver,
            "goal": goal,
            "status": "success (simulated)"
        }
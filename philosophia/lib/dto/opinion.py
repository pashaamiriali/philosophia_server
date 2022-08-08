class Opinion:
    def __init__(self, id: str, content: str, thought: str, observation: str, is_positive: bool):
        self.id = id
        self.content = content
        self.thought = thought
        self.observation = observation
        self.is_positive = is_positive

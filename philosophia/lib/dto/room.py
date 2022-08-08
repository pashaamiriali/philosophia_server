class Room:
    def __init__(self, id: str, name: str, ownerships: list, debates: list, observations: list, ) -> None:
        self.id = id
        self.name = name
        self.ownerships = ownerships
        self.debates = debates
        self.observations = observations

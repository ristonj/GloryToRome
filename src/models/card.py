from .role import Role

class Card:
    def __init__(self,
            name: str,
            role: Role,
            description: str):

        self.name = name
        self.role = role
        self.description = description

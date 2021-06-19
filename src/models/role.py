import typing

class Role:

    def __init__(
            self,
            name: str,
            material: str,
            value: int):

        self.name = name
        self.material = material
        self.value = value
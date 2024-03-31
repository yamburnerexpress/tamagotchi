from Modules.status import Status

class Consumable:
    def __init__(self, name: str, description: str, hp: int, hunger: int, status: Status):
        self.name = name
        self.description = description
        self.hp = hp
        self.hunger = hunger
        self.status = status

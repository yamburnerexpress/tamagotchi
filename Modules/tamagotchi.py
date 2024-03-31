from Modules import Consumable, Status
from Modules.Services.json_manager import init_status
from Modules.statuses.healthy import Healthy

class Tamagotchi:
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name

        self.hp: int = 100
        self.str: int = 20
        self.dex: int = 20
        self.con: int = 20

        self.age: int = 0

        self.hunger: int = 0
        self.fun: int = 0
        self.tiredness: int = 0
        self.anger: int = 0
        self.fight: int = 0
        self.love: int = 0
        self.status: Status = init_status(1)

        self.messages = []

    def feed(self, food: Consumable) -> None:
        self.messages.append(f"{self.first_name} ate some {food.name}!")
        self._lower_hunger(food.hunger)
        self.add_status(food.status)

    def entertain(self, activity) -> None:
        pass

    def sleep(self) -> None:
        pass

    def _lower_hunger(self, hunger: int) -> None:
        self.hunger = max(0, self.hunger - hunger)

    def add_status(self, new_status: Status) -> None:
        self.status = new_status
        self.messages.append(f"{self.first_name} is feeling {self.status.name}!")
        # if self.status.severity < new_status.severity:
        #     self.status = new_status
        #     self.messages.append(f"{self.first_name} is feeling {self.status.name}!")
        # else:
        #     pass

    def update_status(self) -> None:
        # self.messages.append(self.__dict__)
        self.messages.append(f"{self.first_name} is feeling {self.status.name}!")
        is_hurt, hp_message = self._get_hp_message()
        is_tired, tired_message = self._get_tired_message()
        if is_hurt:
            self.messages.append(hp_message)
        if is_tired:
            self.messages.append(tired_message)

    def _get_hp_message(self) -> tuple:
        if 25 < self.hp <= 50:
            return True, f"{self.first_name} is hurt!"
        elif self.hp <= 25:
            return True, f"{self.first_name} is really hurt!!"
        else:
            return False, None

    def _get_tired_message(self) -> tuple:
        if 50 <= self.tiredness < 80:
            return True, f"{self.first_name} is sleepy!"
        elif self.tiredness >= 80:
            return True, f"{self.first_name} is really sleepy!!"
        else:
            return False, None

    def clear_messages(self):
        self.messages = []

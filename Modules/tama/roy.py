from Modules.tamagotchi import Tamagotchi

class Roy(Tamagotchi):
    def __init__(self):
        super().__init__()
        self.name = "Roy"

    def get_stats(self):
        self.messages.append(self.__dict__)

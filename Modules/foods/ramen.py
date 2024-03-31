from Modules.consumable import Consumable
from Modules.statuses.healthy import Healthy

class Ramen(Consumable):
    def __init__(self):
        super().__init__(
            name="Ramen",
            hp=50,
            hunger=50,
            status=Healthy()
        )

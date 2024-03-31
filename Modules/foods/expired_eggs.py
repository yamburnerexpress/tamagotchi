from Modules.consumable import Consumable
from Modules.statuses.barfy import Barfy

class ExpiredEggs(Consumable):
    def __init__(self):
        super().__init__(
            name="Expired Eggs",
            hp=-20,
            hunger=0,
            status=Barfy()
        )

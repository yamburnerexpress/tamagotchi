# from Modules.tamagotchi import Tamagotchi
from Modules.status import Status
from Modules.consumable import Consumable
from collections import namedtuple
import json

TAMA_PATH = "Modules/data/tamas.json"
CONSUMABLE_PATH = "Modules/data/consumables.json"
STATUS_PATH = "Modules/data/statuses.json"

def load_from_json(path: str):
    with open(path) as file:
        x = json.load(
            file,
            object_hook=lambda d: namedtuple('Data', d.keys())(*d.values()))
        return x




def init_food(food_id: int) -> Consumable:
    data = load_from_json(CONSUMABLE_PATH)
    for food in data.foods:
        if food.id == food_id:
            return Consumable(food.name, food.description, food.hp, food.hunger, init_status(food.status.id))

def init_status(status_id: int) -> Status:
    data = load_from_json(STATUS_PATH)
    for status in data.statuses:
        if status.id == status_id:
            return Status(status.name, status.severity, status.is_sick)

def load_all_foods() -> list:
    data = load_from_json(CONSUMABLE_PATH)
    return data.foods

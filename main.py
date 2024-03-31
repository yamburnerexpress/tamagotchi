from Modules import Tamagotchi
from Modules.consumable import Consumable
from Modules.Services.json_manager import load_all_foods, init_food, init_status, load_from_json, TAMA_PATH
from Modules.foods.ramen import Ramen
from Modules.foods.expired_eggs import ExpiredEggs

def init_tamagotchi(tama_id: int) -> Tamagotchi:
    data = load_from_json(TAMA_PATH)
    for tama in data.tamagotchis:
        if tama.id == tama_id:
            return Tamagotchi(tama.first_name, tama.last_name)


roy: Tamagotchi = init_tamagotchi(1)

def game_loop():
    # TODO: every loop, affect fun or tiredness or hunger randomly
    display_main_options()
    print("")
    action = int(input("What do you want to do? "))
    process_main_action(action)

def menu(func):
    def inner1(*args, **kwargs):
        clear_screen()
        func(*args, **kwargs)
    return inner1

def clear_screen() -> None:
    print("\n" * 10)

@menu
def display_main_options() -> None:
    display_messages()
    print(f"1. Check {roy.first_name}'s status")
    print(f"2. Feed {roy.first_name}")
    print(f"3. Pet {roy.first_name}")
    print(f"4. Tuck {roy.first_name} in for a nap")
    if roy.status.is_sick:
        print(f"5. Give {roy.first_name} some medicine")

def process_main_action(selection: int):
    if selection == 1:
        roy.update_status()
    elif selection == 2:
        display_food_options()
        print("")
        action = int(input(f"Which food do you want to feed {roy.first_name}? "))
        process_food_action(action)
    elif selection == 3:
        roy.fun = max(roy.fun + 5, 100)
        roy.love = max(roy.fun + 5, 100)
        roy.messages.append(f"{roy.first_name} liked that!!")
    elif selection == 4:
        # TODO: should refuse if too angry
        roy.tiredness = min(roy.tiredness - 50, 0)
        roy.messages.append(f"{roy.first_name} is snoozing peacefully")
    elif selection == 5:
        roy.add_status(init_status(1))


@menu
def display_food_options() -> None:
    for food in load_all_foods():
        print(f"{food.id}. Feed {roy.first_name} {food.name}")

def get_status() -> None:
    # roy.get_stats()
    roy.update_status()

@menu
def process_food_action(selection: int):
    clear_screen()
    roy.feed(init_food(selection))

def display_messages():
    for message in roy.messages:
        print(f"> {message}")
    print("")
    roy.clear_messages()


if __name__ == "__main__":
    roy.hunger = 40
    roy.tiredness = 51
    while True:
        game_loop()

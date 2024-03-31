from Modules.Services.json_manager import init_tamagotchi, init_food, load_all_foods

# x = init_food(1)
# print(x.__dict__)

x = load_all_foods()
for food in x:
    print(food.name)

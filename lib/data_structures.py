spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_name = [food.get('name') for food in spicy_foods]
    return food_name

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food.get('heat_level') > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name')
        where = food.get('cuisine')
        heat = food.get('heat_level')
        chili = '🌶' * heat
        spicy = f'{name} ({where}) | Heat Level: {chili}'
        print(spicy)
# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    find_cuisine = [food for food in spicy_foods if food['cuisine'] == cuisine]
    return find_cuisine[0]
get_spicy_food_by_cuisine(spicy_foods, 'American')

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get('heat_level') > 5:
            name = food.get('name')
            where = food.get('cuisine')
            heat = food.get('heat_level')
            chili = '🌶' * heat
            spicy = f'{name} ({where}) | Heat Level: {chili}'
            print(spicy)
# print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    heat = [food.get('heat_level') for food in spicy_foods]
    total_heat = sum(heat)
    average = int(total_heat / len(heat))
    return average
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
create_spicy_food(spicy_foods, {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10})

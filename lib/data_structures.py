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
   return [names.get("name")for names in spicy_foods]
    # pass

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food.get("heat_level") > 5]
    # pass

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = "🌶" * spicy_food["heat_level"]
        print(
            f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_level}")     
    # pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
           return food
    
    # pass



def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emoji}")

    
    
    # pass

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average_heat_level = total_heat_level // len(spicy_foods)
    return average_heat_level
    # pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

    # pass

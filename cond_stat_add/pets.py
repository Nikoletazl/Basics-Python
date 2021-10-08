days = int(input())
food_kg = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000
import math
needed_food_dog = days * dog_food
needed_food_cat = days * cat_food
needed_food_turtle = days * turtle_food
total_food = needed_food_dog + needed_food_cat + needed_food_turtle
if total_food <= food_kg:
    left_food = food_kg - total_food
    print(f"{math.floor(left_food)} kilos of food left.")
else:
    needed_food = total_food - food_kg
    print(f"{math.ceil(needed_food)} more kilos of food are needed.")
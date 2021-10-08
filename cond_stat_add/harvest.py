x = int(input())
y = float(input())
z = int(input())
workers = int(input())
import math
total_grape = (x * y)
wine = 0.4 * (total_grape / 2.5)
if wine >= z:
    total_liters = (wine - z)
    liters_per_person = (total_liters / workers)
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(total_liters)} liters left -> {math.ceil(liters_per_person)} liters per person.")
elif wine < z:
    needed_liters = (z - wine)
    print(f"It will be a tough winter! More {math.floor(needed_liters)} liters wine needed.")


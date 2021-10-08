name = input()
budget = float(input())
count_beers = int(input())
count_chips = int(input())
import math
price_beer = 1.20 * count_beers
one_chips = 0.45 * price_beer
total_chips = math.ceil(one_chips * count_chips)
total_sum = price_beer + total_chips
if total_sum <= budget:
    left_money = budget - total_sum
    print(f"{name} bought a snack and has {left_money:.2f} leva left.")
else:
    left_money = total_sum - budget
    print(f"{name} needs {left_money:.2f} more leva!")

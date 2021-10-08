budget = int(input())
season = input()
number_fishermen = int(input())
rent = 0
if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600
if number_fishermen <= 6:
    rent = rent - 0.10 * rent
elif 7 >= number_fishermen <=11:
    rent = rent - 0.15 * rent
elif number_fishermen >= 12:
    rent = rent - 0.25 * rent
if number_fishermen % 2 == 0 and season != "Autumn":
    rent = rent - 0.05 * rent
if budget >= rent:
    left_money = budget - rent
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    need_money = rent - budget
    print(f"Not enough money! You need {need_money:.2f} leva.")
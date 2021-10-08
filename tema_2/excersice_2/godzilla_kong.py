budget = float(input())
count_statists = int(input())
price_per_statists = float(input())
price_decor = 0.1 * budget
price_clothes = count_statists * price_per_statists
if count_statists > 150:
    price_clothes = price_clothes - 0.10 * price_clothes
expenses = price_decor + price_clothes
if expenses > budget:
    print("Not enough money!")
    need_money = expenses - budget
    print(f"Wingard needs {need_money:.2f} leva more.")
else:
    print("Action!")
    left_money = budget - expenses
    print(f"Wingard starts filming with {left_money:.2f} leva left.")
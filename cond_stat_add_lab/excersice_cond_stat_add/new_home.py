type_flowers = input()
count_flowers = int(input())
budget = int(input())
final_price = 0
if type_flowers == "Roses":
    final_price = count_flowers * 5
    if count_flowers > 80:
        final_price = final_price - 0.10 * final_price

elif type_flowers == "Dahlias":
    final_price = count_flowers * 3.80
    if count_flowers > 90:
        final_price = final_price - 0.15 * final_price
elif type_flowers == "Tulips":
    final_price = count_flowers * 2.80
    if count_flowers > 80:
        final_price = final_price - 0.15 * final_price
elif type_flowers == "Narcissus":
    final_price = count_flowers * 3
    if count_flowers < 120:
        final_price = final_price + 0.15 * final_price

elif type_flowers == "Gladiolus":
    final_price = count_flowers * 2.50
    if count_flowers < 80:
        final_price = final_price + 0.2 * final_price
if budget >= final_price:
    left_money = budget - final_price
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {left_money:.2f} leva left.")
else:
    need_money = final_price - budget
    print(f"Not enough money, you need {need_money:.2f} leva more.")

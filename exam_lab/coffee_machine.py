drink_type = input()
sugar = input()
number_of_drinks = int(input())
drink_price = 0
if drink_type == "Espresso":
    if sugar == "Without":
        drink_price = 0.9
        drink_price *= 0.65
    elif sugar == "Normal":
        drink_price = 1
    elif sugar == "Extra":
        drink_price = 1.2
    if number_of_drinks >= 5:
        drink_price *= 0.75
elif drink_type == "Cappuccino":
    if sugar == "Without":
        drink_price = 1
        drink_price *= 0.65
    elif sugar == "Normal":
        drink_price = 1.2
    elif sugar == "Extra":
        drink_price = 1.6
elif drink_type == "Tea":
    if sugar == "Without":
        drink_price = 0.5
        drink_price *= 0.65
    elif sugar == "Normal":
        drink_price = 0.6
    elif sugar == "Extra":
        drink_price = 0.7
total_sum = drink_price * number_of_drinks
if total_sum > 15:
    total_sum *= 0.8
print(f"You bought {number_of_drinks} cups of {drink_type} for {total_sum:.2f} lv.")
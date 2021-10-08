count_joinery = int(input())
range = input()
delivery = input()
price_one_joinery = 0
total_price = 0
if range == "90X130":
    price_one_joinery = 110
    total_price = price_one_joinery * count_joinery
    if 60 >= count_joinery > 30:
        total_price = total_price - 0.05 * total_price
    elif count_joinery > 60:
        total_price = total_price - 0.08 * total_price
    if delivery == "With delivery":
        total_price += 60
elif range == "100X150":
    price_one_joinery = 140
    total_price = price_one_joinery * count_joinery
    if 80 >= count_joinery > 40:
        total_price = total_price - 0.06 * total_price
    elif count_joinery > 80:
        total_price = total_price - 0.1 * total_price
    if delivery == "With delivery":
        total_price += 60
elif range == "130X180":
    price_one_joinery = 190
    total_price = price_one_joinery * count_joinery
    if 50 >= count_joinery > 20:
        total_price = total_price - 0.07 * total_price
    elif count_joinery > 50:
        total_price = total_price - 0.12 * total_price
    if delivery == "With delivery":
        total_price += 60
elif range == "200X300":
    price_one_joinery = 250
    total_price = price_one_joinery * count_joinery
    if 50 >= count_joinery > 25:
        total_price = total_price - 0.09 * total_price
    elif count_joinery > 50:
        total_price = total_price - 0.14 * total_price
    if delivery == "With delivery":
        total_price += 60
if count_joinery > 99:
    total_price = total_price - 0.04 * total_price
    print(f"{total_price:.2f} BGN")
elif count_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")




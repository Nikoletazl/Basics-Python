days = int(input())
room = input()
grade = input()
price = 0
sum = 0
if days < 10:
    if room == "room for one person":
        nights = days - 1
        price = 18 * nights
    elif room == "apartment":
        nights = days - 1
        sum = nights * 25
        price = sum - sum * 0.3
    elif room == "president apartment":
        nights = days - 1
        sum = nights * 35
        price = sum - sum * 0.1
elif 10 <= days <= 15:
    if room == "room for one person":
        nights = days - 1
        price = 18 * nights
    elif room == "apartment":
        nights = days - 1
        sum = nights * 25
        price = sum - sum * 0.35
    elif room == "president apartment":
        nights = days - 1
        sum = nights * 35
        price = sum - sum * 0.15
elif  days > 15:
    if room == "room for one person":
        nights = days - 1
        price = 18 * nights
    elif room == "apartment":
        nights = days - 1
        sum = nights * 25
        price = sum - sum * 0.5
    elif room == "president apartment":
        nights = days - 1
        sum = nights * 35
        price = sum - sum * 0.2
if grade == "positive":
    price += 0.25 * price
    print(f"{price:.2f}")
elif grade == "negative":
    price -= 0.1 * price
    print(f"{price:.2f}")

days = int(input())
room = input()
grade = input()
nights = days - 1
price = 0
discount = 0
if room == "room for one person" and grade == "positive":
    if nights < 10:
        price = nights * 18.00
        discount = price + 0.25 * price
        print(f"{discount:.2f}")
    elif 10 < nights < 15:
        price = nights * 18.00
        discount = price + 0.25 * price
        print(f"{discount:.2f}")
    elif nights > 15:
        price = nights * 18.00
        discount = price + 0.25 * price
        print(f"{discount:.2f}")
if room == "room for one person" and grade == "negative":
    if nights < 10:
        price = nights * 18.00
        discount = price - 0.10 * price
        print(f"{discount:.2f}")
    elif 10 < nights < 15:
        price = nights * 18.00
        discount = price - 0.10 * price
        print(f"{discount:.2f}")
    elif nights > 15:
        price = nights * 18.00
        discount = price - 0.10 * price
        print(f"{discount:.2f}")
if room == "apartment" and grade == "positive":
    if nights < 10:
        price = nights * 25.00
        discount = (price -  (0.3 * price))
        total_discount = discount + 0.25 * discount
        print(f"{total_discount:.2f}")
    elif 10 < nights < 15:
        price = nights * 25.00
        discount = (price -  (0.35 * price))
        total_discount = discount + 0.25 * discount
        print(f"{total_discount:.2f}")
    elif nights > 15:
        price = nights * 25.00
        discount = (price -  (0.5 * price))
        total_discount = discount + 0.25 * discount
        print(f"{total_discount:.2f}")
if room == "apartment" and grade == "negative":
    if nights < 10:
        price = nights * 25.00
        discount = (price -  (0.3 * price))
        total_discount = discount - 0.10 * discount
        print(f"{total_discount:.2f}")
    elif 10 < nights < 15:
        price = nights * 25.00
        discount = (price -  (0.35 * price))
        total_discount = discount - 0.10 * discount
        print(f"{total_discount:.2f}")
    elif nights > 15:
        price = nights * 25.00
        discount = (price -  (0.5 * price))
        total_discount = discount - 0.10 * discount
        print(f"{total_discount:.2f}")
if room == "president apartment" and grade == "positive":
    if nights < 10:
        price = nights * 35.00
        discount = (price -  (0.1 * price))
        total_discount = discount + 0.25 * discount
        print(f"{total_discount:.2f}")
    elif 10 < nights < 15:
        price = nights * 35.00
        discount = (price -  (0.15 * price))
        total_discount = discount + 0.25 * discount
        print(f"{total_discount:.2f}")
    elif nights > 15:
        price = nights * 35.00
        discount = (price -  (0.2 * price))
        total_discount = discount + 0.25 * discount
        print(f"{total_discount:.2f}")
if room == "president apartment" and grade == "negative":
    if nights < 10:
        price = nights * 35.00
        discount = (price -  (0.1 * price))
        total_discount = discount - 0.10 * discount
        print(f"{total_discount:.2f}")
    elif 10 < nights < 15:
        price = nights * 35.00
        discount = (price -  (0.15 * price))
        total_discount = discount - 0.10 * discount
        print(f"{total_discount:.2f}")
    elif nights > 15:
        price = nights * 35.00
        discount = (price -  (0.2 * price))
        total_discount = discount - 0.10 * discount
        print(f"{total_discount:.2f}")
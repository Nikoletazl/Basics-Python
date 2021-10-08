VIP = 499.99
Normal = 249.99
budget = float(input())
category = input()
members = int(input())
transport_money = 0
left_money = 0
ticket = 0
total_money = 0
if 1 <= members <=4:
    transport_money = 0.75 * budget
elif 5 <= members <= 9:
    transport_money = 0.6 * budget
elif 10 <= members <= 24:
    transport_money = 0.5 * budget
elif 25 <= members <= 49:
    transport_money = 0.4 * budget
elif members >= 50:
    transport_money = 0.25 * budget
left_money = budget - transport_money
if  category == "VIP":
    ticket = VIP * members
    if ticket <= left_money:
        total_money = left_money - ticket
        print(f"Yes! You have {total_money:.2f} leva left.")
    else:
        total_money = abs(left_money - ticket)
        print(f"Not enough money! You need {total_money:.2f} leva.")
elif  category == "Normal":
    ticket = Normal * members
    if ticket <= left_money:
        total_money = left_money - ticket
        print(f"Yes! You have {total_money:.2f} leva left.")
    else:
        total_money = abs(left_money - ticket)
        print(f"Not enough money! You need {total_money:.2f} leva.")

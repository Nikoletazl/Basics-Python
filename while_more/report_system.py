total_sum = int(input())
cash = 0
card = 0
cash_sum = 0
card_sum = 0
sum = 0
command = input()
number = 1
while True:
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    price = int(command)
    number += 1
    if number % 2 == 0:
        if price <= 100:
            cash += 1
            cash_sum += price
            sum += price
            print("Product sold!")
        else:
            print("Error in transaction!")
    elif number % 2 != 0:
        if price >= 10:
            card += 1
            card_sum += price
            sum += price
            print("Product sold!")
        else:
            print("Error in transaction!")
    if sum >= total_sum:
        print(f"Average CS: {cash_sum / cash:.2f}")
        print(f"Average CC: {card_sum / card:.2f}")
        break
    command = input()

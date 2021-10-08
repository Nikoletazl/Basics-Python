need_money = float(input())
current_money = float(input())
count_spend_days = 0
count_days = 0
while current_money < need_money:
    actions = input()
    count_days += 1
    sum = float(input())
    if actions == "spend":
        count_spend_days += 1
        current_money -= sum
        if current_money < 0:
            current_money = 0
    elif actions == "save":
        count_spend_days = 0
        current_money += sum
    if count_spend_days == 5:
        print("You can't save the money.")
        print(f"{count_days}")
        break
else:
    print(f"You saved the money for {count_days} days.")
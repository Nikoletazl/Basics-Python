destination = input()
while destination != "End":
    need_money = float(input())
    money = 0
    while money < need_money:
        saved_money = float(input())
        money += saved_money
    else:
        print(f"Going to {destination}!")
    destination = input()
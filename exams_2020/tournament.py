days = int(input())
days_win = 0
days_lose = 0
total = 0
for i in range(1, days + 1):
    current = input()
    current_money = 0
    win = 0
    lose = 0
    while current != "Finish":
        sport = current
        result = input()
        if result == "win":
            current_money += 20
            win += 1
        elif result == "lose":
            lose += 1
        current = input()
    if win > lose:
        total += current_money * 1.10
        days_win += 1
    else:
        total += current_money
        days_lose += 1
if days_win > days_lose:
    total *= 1.2
    print(f"You won the tournament! Total raised money: {total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total:.2f}")

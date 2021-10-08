number = int(input())
bonus = 0
if number <= 100:
    bonus = 5
    total_point = number + bonus
elif number > 1000:
    bonus = 0.1 * number
    total_point = number + bonus
else:
    bonus = 0.2 * number
    total_point = number + bonus
if number % 2 == 0:
    bonus = bonus + 1
    total_point = number + bonus
    print(bonus)
    print(total_point)
elif number % 10 == 5:
    bonus = bonus + 2
    total_point = number + bonus
    print(bonus)
    print(total_point)
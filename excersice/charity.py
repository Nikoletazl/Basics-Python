days = int(input())
bakers = int(input())
cakes = int(input())
gofretti = int(input())
pancakes = int(input())
sum_cakes = cakes * 45
sum_gofretti = gofretti * 5.80
sum_pancakes = pancakes * 3.20
sum_one_day = (sum_cakes + sum_gofretti + sum_pancakes) * bakers
sum_company = sum_one_day * days
sum_expenses = sum_company - (sum_company * 0.125)
print(sum_expenses)
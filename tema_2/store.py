needed_sum = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
puzzle_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2
total_income = number_of_puzzles * puzzle_price + number_of_dolls * dolls_price + number_of_bears * bears_price + number_of_minions * minions_price + number_of_trucks * trucks_price
total_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
if total_toys >= 50:
    total_income *= 0.75
total_income *= 0.9
difference = abs(total_income - needed_sum)
if total_income >= needed_sum:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
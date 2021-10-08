count_locations = int(input())
counter = 0
for locations in range(1, count_locations + 1):
    average_gold_per_day = float(input())
    dig_days = int(input())
    for day in range(1, dig_days + 1):
        gold_per_day = float(input())
        counter += gold_per_day
    average = counter / dig_days
    if average >= average_gold_per_day:
        print(f"Good job! Average gold per day: {average:.2f}.")
    elif average < average_gold_per_day:
        needed_sum = average_gold_per_day - average
        print(f"You need {needed_sum:.2f} gold.")
    counter = 0

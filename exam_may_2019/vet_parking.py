count_days = int(input())
count_hours_per_day = int(input())
current_tax = 0
total_tax = 0
for day in range(1, count_days + 1):
    for hour in range(1, count_hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            tax = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            tax = 1.25
        else:
            tax = 1
        current_tax += tax
        total_tax += tax
    print(f"Day: {day} - {current_tax:.2f} leva")
    current_tax = 0
print(f"Total: {total_tax:.2f} leva")



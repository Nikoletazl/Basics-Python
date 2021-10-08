food = int(input()) * 1000
day_food = input()
total = 0
while day_food != "Adopted":
    total += int(day_food)
    day_food = input()
if total <= food:
    print(f"Food is enough! Leftovers: {food - total} grams.")
else:
    print(f"Food is no"
          f"t enough. You need {total - food} grams more.")
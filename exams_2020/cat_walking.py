min_per_day = int(input())
count_walks = int(input())
calories = int(input())
total_min = min_per_day * count_walks
total_calories = total_min * 5
half = 0.5 * calories
if total_calories >= half:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
elif total_calories < half:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")
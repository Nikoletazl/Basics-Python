record = float(input())
distance = float(input())
time = float(input())
needed_time = 0
import math
goal_time = distance * time
sec = math.floor(distance / 50)
slowing = sec * 30
total_time = goal_time + slowing
if record < total_time or record == total_time:
    needed_time = total_time - record
    print(f"No! He was {needed_time:.2f} seconds slower.")
else:
    total_time
    print(f"Yes! The new record is {total_time:.2f} seconds.")
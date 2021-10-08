hours = int(input())
days = int(input())
overtime_workers = int(input())
import math

overtime = overtime_workers * (2 * days) + ((0.9 * days) * 8)

if overtime >= hours:
   left_hours = overtime - hours
   print(f"Yes!{math.floor(left_hours)} hours left.")
else:
    needed_hours = hours - overtime
    print(f"Not enough time!{math.ceil(needed_hours)} hours needed.")




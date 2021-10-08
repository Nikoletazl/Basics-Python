count_balls = int(input())
points = 0
count_red = 0
count_yellow = 0
count_orange = 0
count_white = 0
count_black = 0
count_others = 0
total_point = 0
import math
for i in range(count_balls):
    colours = input()
    if colours == "red":
        points += 5
        count_red += 1
    elif colours == "orange":
        points += 10
        count_orange += 1
    elif colours == "yellow":
        points += 15
        count_yellow += 1
    elif colours == "white":
        points += 20
        count_white += 1
    elif colours == "black":
        points //= 2
        count_black += 1
        continue
    else:
        points += 0
        count_others += 1
print(f"Total points: {points}")
print(f"Points from red balls: {count_red}")
print(f"Points from orange balls: {count_orange}")
print(f"Points from yellow balls: {count_yellow}")
print(f"Points from white balls: {count_white}")
print(f"Other colors picked: {count_others}")
print(f"Divides from black balls: {count_black}")
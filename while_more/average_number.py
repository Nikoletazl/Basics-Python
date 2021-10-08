n = int(input())
number = 0
count = 0
average = 0
for i in range(n):
    current_number = int(input())
    number += current_number
    count += 1
    average = number / count
print(f"{average:.2f}")
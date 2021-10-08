first = int(input())
second = int(input())
third = int(input())
for number in range(2, first + 1, 2):
    for number2 in range(2, second + 1):
        for number3 in range(2, third + 1, 2):
            if number2 == 2 or number2 == 3 or number2 == 5 or number2 == 7:
                print(f"{number} {number2} {number3}", end=" ")
                print()



n = int(input())
sum_first = 0
sum_second = 0
if n <= 7:
    for number1 in range(1, n):
        for number2 in range(1, n):
            for number3 in range(1, n):
                for number4 in range(1, n):
                    sum_first = number1 + number2
                    sum_second = number3 + number4
                    if sum_first == sum_second:
                        if sum_first % n == 0:
                            print(f"{number1}{number2}{number3}{number4}", end=" ")
if n > 7:
    for number1 in range(1, 10):
        for number2 in range(1, 10):
            for number3 in range(1, 10):
                for number4 in range(1, 10):
                    sum_first = number1 + number2
                    sum_second = number3 + number4
                    if sum_first == sum_second:
                        if n % sum_first == 0:
                            print(f"{number1}{number2}{number3}{number4}", end=" ")

n = int(input())
product = 0
sum = 0
for a in range(1, 10):
    if a <= 9:
        for b in range(9, 10):
            if b >= a:
                for c in range(0, 10):
                    if c <= 9:
                        for d in range(c, 9):
                            if d >= c:
                                pass
    sum = a + b + c + d
    product = a * b * c * d
    if sum == product and n / 100 == 5:
        print(f"{a}{b}{c}{d}")
    if product // sum == 3 and n % 3  == 0:
        print(f"{d}{c}{b}{a}")
    else:
        print("Nothing found")

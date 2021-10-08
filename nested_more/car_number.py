start = int(input())
end = int(input())
sum = 0
for first in range(start, end + 1):
    if first % 2 == 0:
        for second in range(start, end + 1):
            for third in range(start, end + 1):
                sum = second + third
                if sum % 2 == 0:
                    for forth in range(start, end + 1):
                        if first > forth and forth % 2 != 0:
                            print(f"{first}{second}{third}{forth}", end=" ")
    if first % 2 != 0:
        for second in range(start, end + 1):
            for third in range(start, end + 1):
                sum = second + third
                if sum % 2 == 0:
                    for forth in range(start, end + 1):
                        if first > forth and forth % 2 == 0:
                            print(f"{first}{second}{third}{forth}", end=" ")



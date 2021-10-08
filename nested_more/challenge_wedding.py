count_men = int(input())
count_women = int(input())
tables = int(input())
couples = 0
while tables != 0 :
    for men in range(1, count_men + 1):
        for women in range(1, count_women + 1):
            couples += 1
            tables -= 1
            if tables < 0:
                break
            print(f"({men} <-> {women})", end=" ")
    count_men = int(input())
    count_women = int(input())













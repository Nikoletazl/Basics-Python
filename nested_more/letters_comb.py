letter1 = input()
letter2 = input()
letter3 = input()
counter = 0
for first in range(ord(letter1), ord(letter2) + 1):
    if first != ord(letter3):
        for second in range(ord(letter1), ord(letter2) + 1):
            if second != ord(letter3):
                for third in range(ord(letter1), ord(letter2) + 1):
                    if third != ord(letter3) :
                        counter += 1
                        print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")
print(counter, end=" ")

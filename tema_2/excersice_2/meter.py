number = float(input())
unit = input()
result = input()
if unit == "mm":
    result == "m"
    total = number / 1000
elif unit == "mm":
    result == "cm"
    total = number / 100
else:
    unit == "cm"
    result == "m"
    total = number / 100
if unit == "mm":
    result == "cm"
    total = number / 10
elif unit == "m":
    result == "mm"
    total = number * 1000
else:
    unit == "cm"if unit == "cm":
    result == "mm"
    total = number * 10
print(f"{total:.3f}")









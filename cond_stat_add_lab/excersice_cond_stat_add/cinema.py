projection = input()
r = int(input())
c = int(input())
income = 0
if projection == "Premiere":
    income = (r * c) * 12.00
elif projection == "Normal":
    income = (r * c) * 7.50
elif projection == "Discount":
    income = (r * c) * 5
print(f"{income:.2f} leva")
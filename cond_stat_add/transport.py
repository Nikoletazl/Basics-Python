n = int(input())
price = (input())
if n < 20 and price == "day":
    price_taxi = 0.70 + (n * 0.79)
    print(f"{price_taxi:.2f}")
elif n < 20 and price == "night":
    price_taxi = 0.70 + (n * 0.90)
    print(f"{price_taxi:.2f}")
elif n >= 20 and n < 100 and price == "day":
    price_bus = n * 0.09
    print(f"{price_bus:.2f}")
elif n >= 20 and n <= 100 and price == "night":
    price_bus = n * 0.09
    print(f"{price_bus:.2f}")
elif n >= 100 and price == "night":
    price_train = n * 0.06
    print(f"{price_train:.2f}")
elif n >= 100 and price == "day":
    price_train = n * 0.06
    print(f"{price_train:.2f}")
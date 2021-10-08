budget = float(input())
season = input()
price = 0
if budget <= 100 and season == "summer":
    price = 0.30 * budget
    print("Somewhere in Bulgaria")
    print(f"Camp - {price:.2f}")
elif budget <= 100 and season == "winter":
    price = 0.70 * budget
    print("Somewhere in Bulgaria")
    print(f"Hotel - {price:.2f}")
elif budget <= 1000 and season == "summer":
    price = 0.40 * budget
    print("Somewhere in Balkans")
    print(f"Camp - {price:.2f}")
elif budget <= 1000 and season == "winter":
    price = 0.80 * budget
    print("Somewhere in Balkans")
    print(f"Hotel - {price:.2f}")
elif budget > 1000 and season == "summer" or season == "winter":
    price = 0.90 * budget
    print("Somewhere in Europe")
    print(f"Hotel - {price:.2f}")
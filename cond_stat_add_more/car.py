budget = float(input())
season = input()
if budget <= 100:
    category = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = 0.35 * budget
    if season == "Winter":
        type_car = "Jeep"
        price = 0.65 * budget
if 100 < budget <= 500:
    category = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = 0.45 * budget
    elif season == "Winter":
        type_car = "Jeep"
        price = 0.8 * budget
if budget > 500:
    category = "Luxury class"
    type_car = "Jeep"
    price = 0.9 * budget
print(category)
print(f"{type_car} - {price:.2f}")
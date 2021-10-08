season = input()
km_per_month = float(input())
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = 0.75 * km_per_month
    elif season == "Summer":
        salary = 0.9 * km_per_month
    elif season == "Winter":
        salary = 1.05 * km_per_month
if 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = 0.95 * km_per_month
    elif season == "Summer":
        salary = 1.10 * km_per_month
    elif season == "Winter":
        salary = 1.25 * km_per_month
if 10000 < km_per_month <= 20000:
    salary = 1.45 * km_per_month
tax = (salary * 4) - ((0.1 * salary) * 4)
print(f"{tax:.2f}")



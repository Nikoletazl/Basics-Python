city = input()
sells = float(input())
commission = 0
if 0 <= sells <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
elif 500 < sells <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
if 1000 < sells <= 10000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.1
    elif city == "Plovdiv":
        commission = 0.12
elif sells > 10000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145
if commission == 0:
    print("error")
else:
    income = sells * commission
    print(f"{income:.2f}")

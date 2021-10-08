gas = input()
liters_gas = float(input())
if liters_gas < 25:
    if gas == "Diesel":
        print(f"Fill your tank with diesel!")
    elif gas == "Gasoline":
        print(f"Fill your tank with gasoline!")
    elif gas == "Gas":
        print(f"Fill your tank with gas!")
    else:
        print("Invalid fuel!")
elif liters_gas >= 25:
    if gas == "Diesel":
        print(f"You have enough diesel.")
    elif gas == "Gasoline":
        print(f"You have enough gasoline.")
    elif gas == "Gas":
        print(f"You have enough gas.")
    else:
        print("Invalid fuel!")


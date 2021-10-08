gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
type_gas = input()
quantity_gas = float(input())
card = input()
if card == "Yes":
    if type_gas == "Gasoline":
        discount = gasoline_price - 0.18
        total_price = discount * quantity_gas
    elif type_gas == "Diesel":
        discount = diesel_price - 0.12
        total_price = discount * quantity_gas
    elif type_gas == "Gas":
        discount = gas_price - 0.08
        total_price = discount * quantity_gas
    if 0 > quantity_gas < 20:
        print(f"{total_price:.2f} lv.")
    elif 20 <= quantity_gas <= 25:
        discount_total = total_price - 0.08 * total_price
    elif quantity_gas > 25:
        discount_total = total_price - 0.1 * total_price
        print(f"{discount_total:.2f} lv.")

    else:
        discount_total = total - ((total * 0) / 100)
        print(f"{discount_total:.2f} lv.")

elif card == "No":
    if type_gas == "Gasoline":
        total = (gasoline_price * quantity_gas)
    elif type_gas == "Diesel":
        total = (diesel_price * quantity_gas)
    elif type_gas == "Gas":
        total = (gas_price * quantity_gas)

    if 20 <= quantity_gas <= 25:
        discount_no = total - 0.08 * total
        print(f"{discount_no:.2f} lv.")
    elif quantity_gas > 25:
        discount_no = total - 0.1 * total
        print(f"{discount_no:.2f} lv.")
    elif 20 > quantity_gas > 0:
        print(f"{total:.2f} lv.")
    else:
        discount_no = total - ((total * 0) / 100)
        print(f"{discount_no:.2f} lv.")


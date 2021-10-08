# price of raspberry = napolovina po niska ot strawberry
# price of oranges = 40% po niska ot raspberry
# price of bananas = 80% oi niska ot raspberry
# expenses
price_strawberries = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())
total_strawberries = quantity_strawberries * price_strawberries
total_raspberries = quantity_raspberries * (price_strawberries / 2)
price_raspberries = price_strawberries / 2
price_bananas = price_raspberries - 0.8 * price_raspberries
total_bananas = quantity_bananas * price_bananas
price_oranges = price_raspberries - 0.4 * price_raspberries
total_oranges = quantity_oranges * price_oranges
expenses = total_oranges + total_bananas + total_raspberries + total_strawberries
print(expenses)
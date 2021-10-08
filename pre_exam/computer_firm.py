computers = int(input())
total_sales = 0
rate = 0
total_rate = 0
sale1 = 0
sale2 = 0
sale3 = 0
sale4 = 0
sale5 = 0
for number in range(1, computers + 1):
    sales = int(input())
    units = sales % 10
    tens = sales // 10
    if units == 2:
        sale1 = 0
        rate += units
    elif units == 3:
        completed_sales = tens * 0.5
        sale2 += completed_sales
        rate += units
    elif units == 4:
        completed_sales = tens * 0.7
        sale3 += completed_sales
        rate += units
    elif units == 5:
        completed_sales = tens * 0.85
        sale4 += completed_sales
        rate += units
    elif units == 6:
        completed_sales = tens * 1
        sale5 += completed_sales
        rate += units
total_sales = sale1 + sale2 + sale3 + sale4 + sale5
total_rate = rate / computers
print(f"{total_sales:.2f}")
print(f"{total_rate:.2f}")





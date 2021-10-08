number1 = int(input())
number2 = int(input())
operator = input()
if operator == "+":
    sum = number1 + number2
    if sum % 2 == 0:
        print(f"{number1} + {number2} = {sum} - even")
    else:
        print(f"{number1} + {number2} = {sum} - odd")
elif operator == "-":
    diff = number1 - number2
    if diff % 2 == 0:
        print(f"{number1} - {number2} = {diff} - even")
    else:
        print(f"{number1} - {number2} = {diff} - odd")
elif operator == "*":
    product = number1 * number2
    if product % 2 == 0:
        print(f"{number1} * {number2} = {product} - even")
    else:
        print(f"{number1} * {number2} = {product} - odd")
elif operator == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        division = number1 / number2
        print(f"{number1} / {number2} = {division:.2f}")
elif operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        leftover = number1 % number2
        print(f"{number1} % {number2} = {leftover}")

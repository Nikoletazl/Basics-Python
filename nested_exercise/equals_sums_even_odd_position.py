start_number = int(input())
end_number = int(input())
for number in range(start_number, end_number + 1):
    units = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000 % 10
    tens_thousands = number // 10000 % 10
    hundreds_thousands = number // 100000
    sum_even = units + hundreds + tens_thousands
    sum_odd = tens + thousands + hundreds_thousands
    if sum_odd == sum_even:
        print(number, end=" ")


juniors = int(input())
seniors = int(input())
track = input()
if track == "trail":
   tax_jun = 5.50
   tax_sen = 7
   total_sum = juniors * tax_jun + seniors * tax_sen
   expenses = total_sum - (0.05 * total_sum)
elif track == "cross-country":
    tax_jun = 8
    tax_sen = 9.50
    total_sum = juniors * tax_jun + seniors * tax_sen
    expenses = total_sum - (0.05 * total_sum)
    if seniors + juniors >= 50:
        tax_jun = 8 - (8 * 0.25)
        tax_sen = 9.50 - (9.50 * 0.25)
        total_sum = juniors * tax_jun + seniors * tax_sen
        expenses = total_sum - (0.05 * total_sum)
elif track == "downhill":
    tax_jun = 12.25
    tax_sen = 13.75
    total_sum = juniors * tax_jun + seniors * tax_sen
    expenses = total_sum - (0.05 * total_sum)
elif track == "road":
    tax_jun = 20
    tax_sen = 21.50
    total_sum = juniors * tax_jun + seniors * tax_sen
    expenses = total_sum - (0.05 * total_sum)
print(f"{expenses:.2f}")




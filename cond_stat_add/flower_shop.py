magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cactus_price = 8
count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cactus = int(input())
price_gift = float(input())
import math
# ot obshtata suma 5% danuk
sum = count_magnolias * magnolias_price + count_hyacinths * hyacinths_price + count_roses * roses_price + count_cactus * cactus_price
tax = (5 * sum) / 100
total_sum = sum - tax

if 0 < total_sum <= price_gift:
    needed_sum = price_gift - total_sum
    print(f"She will have to borrow {math.ceil(needed_sum)} leva.")

elif total_sum > price_gift or total_sum == 0:
    left_sum = total_sum - price_gift
    print(f"She is left with {math.floor(left_sum)} leva.")


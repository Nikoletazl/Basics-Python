pens = 5.80
markers = 7.20
detergent = 1.20
count_pens = int(input())
count_markers = int(input())
derergent_liters = float(input())
percent_discount = int(input())
price_pens = count_pens * pens
price_markers = count_markers * markers
price_detergent = derergent_liters * detergent
sum = price_pens + price_markers + price_detergent
discount_price = sum - ((sum * percent_discount) / 100)
print(f"{discount_price:.3f}")
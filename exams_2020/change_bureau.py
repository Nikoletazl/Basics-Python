count_bitcoins = int(input())
count_chinese = float(input())
comission = float(input())
dolars = 1.76
chinese = 0.15
bitcoins = 1168
euro = 1.95
comission_price = 0
total = 0
bitcoins_price = bitcoins * count_bitcoins
chinese_price = (chinese * count_chinese) * dolars
euro_price = (bitcoins_price + chinese_price) / euro
comission_per = comission / 100
comission_price = (euro_price * comission_per) - comission_price
total = euro_price - comission_price
print(f"{total:.2f}")
mackerel_price_kg = float(input())
sprat_price_kg = float(input())
bonito = float(input())
scad = float(input())
mussel = int(input())
#cena na palamuda
total_bonito = mackerel_price_kg + mackerel_price_kg * 0.60
price_bonito = bonito * total_bonito
#cena safrid
total_scad = sprat_price_kg + sprat_price_kg * 0.80
price_scad = scad * total_scad
#cena midi
price_mussel = mussel * 7.50
expenses = price_mussel + price_scad + price_bonito
print("%.2f" % expenses)

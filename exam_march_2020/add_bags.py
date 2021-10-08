#taksi bagaj
# do 10kg = 0.2 * price bagaj nad 20kg
# mejdu 10 i 20 wkl - 0.5 * price bagaj nad 20kg
# nad 20kg ot konzolata
#dni
#poveche ot 30 dni cenata na bagaja se oskupqva s 10%
#mejdu 7 i 30 dni vkl - cenata na bagaja se osk s 15%
# po malko ot 7 dni - cenata na bagaja se osk s 40%
price_luggage_20 = float(input())
kg_luggage = float(input())
days_to_jorney = int(input())
count_luggages = int(input())
tax_luggage = 0
total_price = 0
if kg_luggage < 10:
    tax_luggage = price_luggage_20 * 0.2
elif 10 <= kg_luggage <= 20:
    tax_luggage = 0.5 * price_luggage_20
elif kg_luggage > 20:
    tax_luggage = price_luggage_20
if days_to_jorney > 30:
    total_price = (tax_luggage + tax_luggage * 0.1) * count_luggages
elif 7 <= days_to_jorney <= 30:
    total_price = (tax_luggage + tax_luggage * 0.15) * count_luggages
elif 7 > days_to_jorney:
    total_price = (tax_luggage + tax_luggage * 0.4) * count_luggages
print(f"The total price of bags is: {total_price:.2f} lv.")
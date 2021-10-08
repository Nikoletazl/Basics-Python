month = input()
night = int(input())

studio = 76
apartment = 77
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if night > 14:
        studio *= 0.7
    elif night > 7:
        studio *= 0.95
elif month == "June" or month == 'September':
    studio = 75.20
    apartment = 68.70
    if night > 14:
        studio *= 0.8

if night > 14:
    apartment *= 0.9

print(f'Apartment: {night * apartment:.2f} lv.')
print(f'Studio: {night * studio:.2f} lv.')
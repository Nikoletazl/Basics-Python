team = input()
souvenirs = input()
count_souvenirs = int(input())
if souvenirs == "flags":
    if team == "Argentina":
        price = count_souvenirs * 3.25
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Brazil":
        price = count_souvenirs * 4.20
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Croatia":
        price = count_souvenirs * 2.75
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Denmark":
        price = count_souvenirs * 3.10
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    else:
        print("Invalid country!")
elif souvenirs == "caps":
    if team == "Argentina":
        price = count_souvenirs * 7.20
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Brazil":
        price = count_souvenirs * 8.50
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Croatia":
        price = count_souvenirs * 6.90
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Denmark":
        price = count_souvenirs * 6.50
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    else:
        print("Invalid country!")
elif souvenirs == "posters":
    if team == "Argentina":
        price = count_souvenirs * 5.10
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Brazil":
        price = count_souvenirs * 5.35
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Croatia":
        price = count_souvenirs * 4.95
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Denmark":
        price = count_souvenirs * 4.80
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    else:
        print("Invalid country!")
elif souvenirs == "stickers":
    if team == "Argentina":
        price = count_souvenirs * 1.25
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Brazil":
        price = count_souvenirs * 1.20
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Croatia":
        price = count_souvenirs * 1.10
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    elif team == "Denmark":
        price = count_souvenirs * 0.90
        print(f'Pepi bought {count_souvenirs} {souvenirs} of {team} for {price:.2f} lv.')
    else:
        print("Invalid country!")
else:
    print("Invalid stock!")

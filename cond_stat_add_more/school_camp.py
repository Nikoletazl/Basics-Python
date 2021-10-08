season = input()
sex = input()
students_count = int(input())
nights_count = int(input())
if season == "Winter":
    if sex == "boys":
        sport = "Judo"
        price = nights_count * 9.60 * students_count
    elif sex == "girls":
        sport = "Gymnastics"
        price = nights_count * 9.60 * students_count
    elif sex == "mixed":
        sport = "Ski"
        price = nights_count * 10 * students_count
    if students_count >= 50:
        total_price = price - (0.5 * price)
    elif 20 >= students_count < 50:
        total_price = price - (0.15 * price)
    elif 10 >= students_count < 20:
        total_price = price - (0.05 * price)
if season == "Summer":
    if sex == "boys":
        sport = "Football"
        price = nights_count * 15 * students_count
    elif sex == "girls":
        sport = "Volleyball"
        price = nights_count * 15 * students_count
    elif sex == "mixed":
        sport = "Swimming"
        price = nights_count * 20 * students_count
    if students_count >= 50:
        total_price = price - (0.5 * price)
    elif 20 >= students_count < 50:
        total_price = price - (0.15 * price)
    elif 10 >= students_count < 20:
        total_price = price - (0.05 * price)
if season == "Spring":
    if sex == "boys":
        sport = "Tennis"
        price = nights_count * 7.20 * students_count
    elif sex == "girls":
        sport = "Athletics"
        price = nights_count * 7.20 * students_count
    elif sex == "mixed":
        sport = "Cycling"
        price = nights_count * 9.50 * students_count
    if students_count >= 50:
        total_price = price - (0.5 * price)
    elif 20 >= students_count < 50:
        total_price = price - (0.15 * price)
    elif 10 >= students_count < 20:
        total_price = price - (0.05 * price)

print(f"{sport} {total_price:.2f} lv.")

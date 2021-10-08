number_of_groups = int(input())
mousalla_climbers = 0
monblan_climbers = 0
kilimandjarp_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for group in range(number_of_groups):
    currents_number_of_climbers = int(input())
    if currents_number_of_climbers <= 5:
        mousalla_climbers += currents_number_of_climbers
    elif currents_number_of_climbers <= 12:
        monblan_climbers += currents_number_of_climbers
    elif currents_number_of_climbers <= 25:
        kilimandjarp_climbers += currents_number_of_climbers
    elif currents_number_of_climbers <= 40:
        k2_climbers += currents_number_of_climbers
    elif currents_number_of_climbers > 40:
        everest_climbers += currents_number_of_climbers
    total_climbers += currents_number_of_climbers
mousalla_per = mousalla_climbers / total_climbers * 100
monblan_per = monblan_climbers / total_climbers * 100
kilimandjarp_per = kilimandjarp_climbers / total_climbers * 100
k2_per = k2_climbers / total_climbers * 100
everest_per = everest_climbers / total_climbers * 100
print(f"{mousalla_per:.2f}%")
print(f"{monblan_per:.2f}%")
print(f"{kilimandjarp_per:.2f}%")
print(f"{k2_per:.2f}%")
print(f"{everest_per:.2f}%")
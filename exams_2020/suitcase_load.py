capacity = float(input())
command = input()
count_suitcase = 0
total = 0
while True:
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    suitcase = float(command)
    count_suitcase += 1
    if count_suitcase % 3 == 0:
        suitcase += 0.1 * suitcase
    capacity -= suitcase
    if capacity < 0:
        count_suitcase -= 1
        print("No more space!")
        break
    command = input()
print(f"Statistic: {count_suitcase} suitcases loaded.")

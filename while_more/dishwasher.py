detergent = int(input()) * 750
command = input()
count_full = 0
count_plates = 0
count_pots = 0
last_dish = 0
dishes = 0
pots = 0
plates = 0
is_enough = True
while True:
    if command == "End":
        break
    dishes = int(command)
    count_full += 1
    last_dish = dishes
    if count_full % 3 != 0:
        count_plates += dishes
        dishes *= 5
        detergent -= dishes
    if count_full % 3 == 0:
        count_pots += dishes
        dishes *= 15
        detergent -= dishes
    if detergent <= 0:
        is_enough = False
        break
    command = input()
if detergent < last_dish:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
if detergent >= last_dish:
    print("Detergent was enough!")
    print(f"{count_plates} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")







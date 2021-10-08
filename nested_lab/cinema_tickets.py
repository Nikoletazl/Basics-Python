counter_standard = 0
counter_kid = 0
counter_student = 0
while True:
    film = input()
    if film == "Finish":
        break
    capacity = int(input())
    tickets_sold = 0
    while capacity > tickets_sold:
        ticket_type = input()
        if ticket_type == "End":
            break
        tickets_sold += 1
        if ticket_type == "standard":
            counter_standard += 1
        elif ticket_type == "kid":
            counter_kid += 1
        elif ticket_type == "student":
            counter_student += 1
    print(f"{film} - {tickets_sold / capacity * 100:.2f}% full.")
ticket_counter = counter_standard + counter_kid + counter_student
print(f"Total tickets: {ticket_counter}")
print(f"{counter_student / ticket_counter * 100:.2f}% student tickets.")
print(f"{counter_standard / ticket_counter * 100:.2f}% standard tickets.")
print(f"{counter_kid / ticket_counter * 100:.2f}% kids tickets.")
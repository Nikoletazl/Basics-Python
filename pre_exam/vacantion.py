count_people = int(input())
count_nights = int(input())
count_cards = int(input())
count_tickets = int(input())
sum_one_person = count_nights * 20
sum_cards = count_cards * 1.60
tickets = count_tickets * 6
total_sum_one = sum_one_person + sum_cards + tickets
group_sum = total_sum_one * count_people
end_sum = group_sum + 0.25 * group_sum
print(f"{end_sum:.2f}")
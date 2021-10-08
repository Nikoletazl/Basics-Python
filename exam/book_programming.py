price_one_print_page = float(input())
price_one_print_coverage = float(input())
discount_print_paper = int(input())
pay_designer = float(input())
per_paid_team = int(input())
start_sum = (price_one_print_page * 899) + (price_one_print_coverage * 2)
percent_paper = discount_print_paper / 100
percent_team = per_paid_team / 100
discount = start_sum - (percent_paper * start_sum)
designer_sum = pay_designer + discount
end_sum = designer_sum - (designer_sum * percent_team)
print(f"Avtonom should pay {end_sum:.2f} BGN.")
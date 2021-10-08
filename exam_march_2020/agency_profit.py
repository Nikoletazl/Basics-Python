name_company = input()
tickets_adults = int(input())
children_tickets = int(input())
one_ticket_adult = float(input())
tax = float(input())
one_ticket_children = one_ticket_adult - 0.7 * one_ticket_adult
price_tax_adult = one_ticket_adult + tax
price_tax_children = one_ticket_children + tax
total_price = (children_tickets * price_tax_children) + (tickets_adults * price_tax_adult)
earnings = 0.2 * total_price

print(f"The profit of your agency from {name_company} tickets is {earnings:.2f} lv.")
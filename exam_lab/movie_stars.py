budget = float(input())
there_is_budget = True
command = input()
while command != "ACTION":
    actor_name = command
    actor_salary = 0
    if len(actor_name) > 15:
        actor_salary = budget * 0.2
    else:
        actor_salary = float(input())
    budget -= actor_salary
    if budget < 0:
        there_is_budget = False
        break
    command = input()
if there_is_budget:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")

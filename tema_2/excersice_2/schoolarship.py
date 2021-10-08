income = float(input())
average_success = float(input())
min_salary = float(input())
import math
if income < min_salary and average_success > 4.5:
   social_scholarship = 0.35 * min_salary
   print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif average_success >= 5.5:
    ex_scholarship = average_success * 25
    print(f"You get a scholarship for excellent results {math.floor(ex_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")


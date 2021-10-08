year = input()
p = int(input())
h = int(input())
import math
if year == "leap":
   weekends = 48
   weekends_at_home = 48 - h
   weekends_at_sofia = weekends_at_home * 0.75
   holiday = p * (2 / 3)
   total_week_hol = weekends_at_sofia + h + holiday
   more = 0.15 * total_week_hol
   whole_year = total_week_hol + more
   print(f"{math.floor(whole_year)}")
elif year == "normal":
    weekends = 48
    weekends_at_home = 48 - h
    weekends_at_sofia = weekends_at_home * 0.75
    holiday = p * (2 / 3)
    total_week_hol = weekends_at_sofia + h + holiday


    print(f"{math.floor(total_week_hol)}")



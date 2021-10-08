hour = int(input())
minutes = int(input())
time_in_minutes = hour * 60 + minutes
time_after_in_min = time_in_minutes + 15
final_hour = time_after_in_min // 60
final_min = time_after_in_min % 60
if final_hour == 24:
    final_hour = 0
if final_min < 10:
    print(f"{final_hour}:0{final_min}")
else:
    print(f"{final_hour}:{final_min}")

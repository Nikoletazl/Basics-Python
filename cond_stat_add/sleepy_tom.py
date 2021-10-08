days_off = int(input())
working_days = 365 - days_off
days_off_time = days_off * 127
working_days_time = working_days * 63
game_time = days_off_time + working_days_time
if game_time < 30000:
    diff_normal = 30000 - game_time
    min_in_hours = diff_normal // 60
    hours_in_min = (diff_normal % 60)
    print("Tom sleeps well")
    print(f"{min_in_hours} hours and {hours_in_min} minutes less for play")
elif game_time > 30000:
    diff_normal = game_time - 30000
    min_in_hours = diff_normal // 60
    hours_in_min = diff_normal % 60
    print("Tom will run away")
    print(f"{min_in_hours} hours and {hours_in_min} minutes more for play")
lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = lenght * width * height
volume_liters = volume / 1000
occupied_part = percent / 100
need_liters = volume_liters * (1 - occupied_part)
print(need_liters)
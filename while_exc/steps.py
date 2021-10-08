command = input()
target = 10000
total_steps = 0
while command != "Going home":
    total_steps += int(command)
    if total_steps >= target:
        break
    command = input()
else:
    steps_to_home = int(input())
    total_steps += steps_to_home
if total_steps >= target:
    print("Goal reached! Good job!")
    print(f"{total_steps - target} steps over the goal!")
else:
    print(f"{target - total_steps} more steps to reach goal.")
sum_tshirt = float(input())
goal_sum = float(input())
shorts = sum_tshirt * 0.75
socks = shorts * 0.2
shoes = (sum_tshirt + shorts) * 2
total_sum = sum_tshirt + shorts + socks + shoes
discount = total_sum - (total_sum * 0.15)
if discount >= goal_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discount:.2f} lv.")
else:
    needed_money = goal_sum - discount
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money:.2f} lv. more.")
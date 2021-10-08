best_player = ""
best_score = 0
player_name = ""
while player_name != "END":
    player_name = input()
    if player_name == "END":
        break
    current_goals = int(input())
    if current_goals > best_score:
        best_score = current_goals
        best_player = player_name
    if best_score >= 10:
        break
print(f"{best_player} is the best player!")
if best_score >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")



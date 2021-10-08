won_matches = 0
lost_matches = 0
total_matches = 0
command = input()
while command != "End of tournaments":
    current_tour_name = command
    number_of_games = int(input())
    for current_game in range(1, number_of_games + 1):
        total_matches += 1
        desi_team = int(input())
        other_team = int(input())
        diff = abs(desi_team - other_team)
        if desi_team > other_team:
            won_matches += 1
            print(f"Game {current_game} of tournament {current_tour_name}: win with {diff} points.")
        else:
            lost_matches += 1
            print(f"Game {current_game} of tournament {current_tour_name}: lost with {diff} points.")
    command = input()
won_matches_per = won_matches / total_matches * 100
lost_matches_per = lost_matches / total_matches * 100
print(f"{won_matches_per:.2f}% matches win")
print(f"{lost_matches_per:.2f}% matches lost")

from mpmath import convert

with open('input_data.txt') as f:
    lines = f.readlines()

list_of_players = []
for i in range(1, len(lines)):
    list_of_players.append(lines[i].strip('\n').split(" "))
print(list_of_players)

total_points = []
for i in range(len(list_of_players)):
    two_points = int(list_of_players[i][-3]) * 2
    three_points = int(list_of_players[i][-2]) * 3
    free_throws = int(list_of_players[i][-1])
    total = two_points + three_points + free_throws
    total_points.append(total)

max_points = max(total_points)


def player_scored_most_points(total_points: list[int]):
    """Check if given list contains any duplicates"""
    max_score = max(total_points)
    list_of_players_with_max_points = []
    for i, value in enumerate(total_points):
        if max_score == value:
            list_of_players_with_max_points.append(list_of_players[i][0])
    min_player_number = min(list_of_players_with_max_points)
    output_1 = f"Player who scored most points is " \
               f"{min_player_number}"
    print(output_1)
    with open('input_data.txt', "w") as f:
        f.write(output_1)
        f.close()


def player_played_least_time(list_of_players: list):
    """Check players with the least time of the game"""
    second_converter = [int(list_of_players[i][1]) * 60 + int(list_of_players[i][2]) for i in
                        range(len(list_of_players))]
    list_of_players_indexes = [i for i, x in enumerate(second_converter) if x == min(second_converter)]
    highest_player_number = max([int(list_of_players[i][0]) for i in list_of_players_indexes])
    output_2 = f"Player who played the least time " \
               f"{highest_player_number}"
    print(output_2)
    with open('input_data.txt', "a") as f:
        f.write("\n")
        f.write(str(output_2))
        f.close()


total_three_points = []
for i in range(len(list_of_players)):
    three_points = int(list_of_players[i][-2]) * 3
    total_three_points.append(three_points)


def player_scored_most_three_points(total_three_points: list[int]):
    """Check if given list contains any duplicates"""
    max_score = max(total_three_points)
    list_of_players_with_max_three_points = []
    for i, value in enumerate(total_three_points):
        if max_score == value:
            list_of_players_with_max_three_points.append(list_of_players[i][0])
    min_player_number = min(list_of_players_with_max_three_points)
    output_3 = f"Player who scored most three points is " \
               f"{min_player_number}"
    print(output_3)
    print(total_three_points)
    with open('input_data.txt', "a") as f:
        f.write("\n")
        f.write(str(output_3))
        f.close()



total_two_points = []
for i in range(len(list_of_players)):
    two_points = int(list_of_players[i][-3]) * 2
    total_two_points.append(two_points)


def sum_of_two_points(total_two_points: list[int]):
    """Sum of points scored by throwing two-points"""
    output_4 = f"Players get {sum(total_two_points)} by throwing two-points"
    print(output_4)
    with open('input_data.txt', "a") as f:
        f.write("\n")
        f.write(str(output_4))
        f.close()


total_free_points = []
for i in range(len(list_of_players)):
    free_throws = int(list_of_players[i][-1])
    total_free_points.append(free_throws)


def sum_of_free_throw_points(total_free_points: list[int]):
    """Sum of points scored by throwing free-throws"""
    output_5 = f'Players get {sum(total_free_points)} by throwing free-throws'
    print(output_5)
    with open('input_data.txt', "a") as f:
        f.write("\n")
        f.write(str(output_5))
        f.close()


def sum_of_total_points(total_points: list[int]):
    """Sum of points during all game"""
    output_6 = f"Players get {sum(total_points)} during all game"
    print(output_6)
    with open('input_data.txt', "a") as f:
        f.write("\n")
        f.write(str(output_6))
        f.close()


player_scored_most_points(total_points)
player_played_least_time(list_of_players)
player_scored_most_three_points(total_three_points)
sum_of_two_points(total_two_points)
sum_of_free_throw_points(total_free_points)
sum_of_total_points(total_points)

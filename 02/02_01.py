
with open("input.txt") as f:
    input = f.readlines()

MAX_VALUES = {
    "red": 12,
    "green": 13,
    "blue": 14
}

result = 0
for game in input:

    game = game.strip()
    game_elements = game.split(":")

    game_id = int(game_elements[0].replace("Game ", ""))
    correct_game = True

    rounds = game_elements[1].strip().split(";")

    for round in rounds:
        if not correct_game:
            break

        round = round.strip().split(",")

        for cubes in round:
            if not correct_game:
                break

            cubes_elements = cubes.strip().split()
            number_of_cubes = int(cubes_elements[0])
            cube_color = cubes_elements[1]
            if number_of_cubes > MAX_VALUES[cube_color]:
                correct_game = False

    if correct_game:
        result += game_id

print(result)

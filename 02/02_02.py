
from functools import reduce

with open("input.txt") as f:
    input = f.readlines()

result = 0
for game in input:

    game = game.strip()
    game_elements = game.split(":")

    game_id = int(game_elements[0].replace("Game ", ""))

    rounds = game_elements[1].strip().split(";")

    max_cubes = {
        "red": -1,
        "green": -1,
        "blue": -1
    }

    for round in rounds:
        round = round.strip().split(",")

        for cubes in round:
            cubes_elements = cubes.strip().split()
            number_of_cubes = int(cubes_elements[0])
            cube_color = cubes_elements[1]
            if number_of_cubes > max_cubes[cube_color]:
                max_cubes[cube_color] = number_of_cubes

    result += reduce((lambda x, y: x * y), max_cubes.values())

print(result)

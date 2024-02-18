
from itertools import combinations

import numpy as np
from tqdm import tqdm

def get_blank_indexes(matrix, axis=0):
    sum_vector = np.sum(matrix, axis=axis)
    return set(np.where(sum_vector == 0)[0])

with open("./input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]


map_matrix = np.zeros((len(input), len(input[0])))

star_value = 1
star_positions = list()
row = 0
for line in input:
    col = 0
    for char in line:
        if char == "#":
            star_positions.append((row, col))
            map_matrix[row, col] = star_value
            star_value += 1
        col += 1
    row += 1

blank_cols = get_blank_indexes(map_matrix)
blank_rows = get_blank_indexes(map_matrix, axis=1)

pairs = [(i, j) for i, j in combinations(range(len(star_positions)), 2)]
print(len(pairs))

res = 0
for pair_positions in tqdm(pairs):

    star_tuple = star_positions[pair_positions[0]]
    star_row = star_tuple[0]
    star_col = star_tuple[1]

    compare_tuple = star_positions[pair_positions[1]]
    compare_row = compare_tuple[0]
    compare_col = compare_tuple[1]

    distance = (
        np.abs(star_row-compare_row) +
        # Add empty rows expansion weight times - 1 (because already added in the np.abs)
        len([
            x for x in range(
                min(star_row, compare_row)+1, max(star_row, compare_row), 1
            ) if x in blank_rows
        ]) * 999999
    )

    distance += (
        np.abs(star_col-compare_col) +
        # Same with cols
        len([
            x for x in range(
                min(star_col, compare_col)+1, max(star_col, compare_col), 1
            ) if x in blank_cols
        ]) * 999999
    )

    res += distance

print(res)

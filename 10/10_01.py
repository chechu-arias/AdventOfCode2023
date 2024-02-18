
import numpy as np

def change_animal_start_pipe():

    up_relevant = False
    if map_matrix[start_animal_row - 1, start_animal_col] in [2, 6, 7]:
        up_relevant = True

    down_relevant = False
    if map_matrix[start_animal_row + 1, start_animal_col] in [2, 4, 5]:
        down_relevant = True

    left_relevant = False
    if map_matrix[start_animal_row, start_animal_col - 1] in [3, 4, 7]:
        left_relevant = True

    right_relevant = False
    if map_matrix[start_animal_row, start_animal_col + 1] in [3, 5, 6]:
        right_relevant = True

    if up_relevant:
        if down_relevant:
            map_matrix[start_animal_row, start_animal_col] = 2
        elif left_relevant:
            map_matrix[start_animal_row, start_animal_col] = 5
        elif right_relevant:
            map_matrix[start_animal_row, start_animal_col] = 4

    elif down_relevant:
        if left_relevant:
            map_matrix[start_animal_row, start_animal_col] = 6
        elif right_relevant:
            map_matrix[start_animal_row, start_animal_col] = 7

    else:
        map_matrix[start_animal_row, start_animal_col] = 3

def up(row, col):
    return row-1, col

def down(row, col):
    return row+1, col

def left(row, col):
    return row, col-1

def right(row, col):
    return row, col+1

def movement(previous_row, previous_col, current_row, current_col):
    current_type = map_matrix[current_row, current_col]
    if current_type == 2:
        if previous_row > current_row:
            return up(current_row, current_col)
        else:
            return down(current_row, current_col)
    elif current_type == 3:
        if previous_col > current_col:
            return left(current_row, current_col)
        else:
            return right(current_row, current_col)
    elif current_type == 4:
        if current_row > previous_row:
            return right(current_row, current_col)
        else:
            return up(current_row, current_col)
    elif current_type == 5:
        if current_row > previous_row:
            return left(current_row, current_col)
        else:
            return up(current_row, current_col)
    elif current_type == 6:
        if current_col > previous_col:
            return down(current_row, current_col)
        else:
            return left(current_row, current_col)
    elif current_type == 7:
        if previous_col > current_col:
            return down(current_row, current_col)
        else:
            return right(current_row, current_col)



with open("./input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

char_to_int = {
    ".": 0,
    "S": 1,
    "|": 2,
    "-": 3,
    "L": 4,
    "J": 5,
    "7": 6,
    "F": 7
}

map_matrix = np.zeros((len(input[0]), len(input)))

start_animal_row = -1
start_animal_col = -1

row = 0
for line in input:
    col = 0
    for char in line:
        if char == "S":
            start_animal_row = row
            start_animal_col = col
        map_matrix[row, col] = char_to_int[char]
        col += 1
    row += 1

current_animal_row = start_animal_row
current_animal_col = start_animal_col

change_animal_start_pipe()

previous_animal_row, previous_animal_col = current_animal_row, current_animal_col
current_animal_row, current_animal_col = movement(current_animal_row, current_animal_col, current_animal_row, current_animal_col)

movements = 1
while current_animal_row != start_animal_row or current_animal_col != start_animal_col:
    aux_row, aux_col = movement(previous_animal_row, previous_animal_col, current_animal_row, current_animal_col)
    previous_animal_row, previous_animal_col = current_animal_row, current_animal_col
    current_animal_row, current_animal_col = aux_row, aux_col
    movements += 1


print(movements//2 + movements % 2)

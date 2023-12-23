
from functools import reduce

def get_row_number_groups(row, index):
    if index == 0 or index == len(row):
        left = index - 1
        if index == 0:
            left = index
        if row[left].isnumeric() or row[left+1].isnumeric():
            return 1
        return 0

    left = row[index-1]
    center = row[index]
    right = row[index+1]
    if left.isnumeric() and not center.isnumeric() and right.isnumeric():
        return 2
    elif left.isnumeric() or center.isnumeric() or right.isnumeric():
        return 1
    return 0


def get_row_numbers_side(row, index):
    res = list()
    if index == 0:
        one_index = index
    else:
        one_index = index - 1

    other_index = one_index + 1
    left_index = one_index
    right_index = other_index

    if row[one_index].isnumeric():
        while left_index > 0 and row[left_index].isnumeric():
            left_index -= 1

    if row[other_index].isnumeric():
        while right_index < len(row) and row[right_index].isnumeric():
            right_index += 1

    if not row[left_index].isnumeric():
        left_index += 1

    if left_index != one_index and right_index != other_index:
        res.append(row[left_index:right_index])
    elif left_index != one_index:
        res.append(row[left_index:one_index])
    elif right_index != other_index:
        res.append(row[other_index:right_index])

    return res


def get_row_numbers(row, index):
    res = list()
    if index == 0 or index == len(row):
        res = get_row_numbers_side(row, index)

    else:
        left = row[index-1]
        center = row[index]
        right = row[index+1]
        if left.isnumeric() and not center.isnumeric() and right.isnumeric():

            left_index = index - 1
            while left_index > 0 and row[left_index].isnumeric():
                left_index -= 1

            right_index = index + 1
            while right_index < len(row) and row[right_index].isnumeric():
                right_index += 1

            if not row[left_index].isnumeric():
                left_index += 1

            res.append(row[left_index:(index)])
            res.append(row[(index+1):right_index])

        elif left.isnumeric() or center.isnumeric() or right.isnumeric():

            if left.isnumeric():
                left_index = index - 1
            elif center.isnumeric():
                left_index = index
            else:
                left_index = index + 1

            right_index = left_index

            while left_index > 0 and row[left_index].isnumeric():
                left_index -= 1
            while right_index < len(row) and row[right_index].isnumeric():
                right_index += 1

            if not row[left_index].isnumeric():
                left_index += 1

            res.append(row[left_index:right_index])

    if len(res) == 0:
        return 1

    return reduce((lambda x, y: x * y), list(map(int, res)))


def compute_numbers_around(row, column):

    n_numbers_around = 0
    current_line = input[row]

    if row != 0:
        upper_row = input[row-1].strip()
        n_numbers_around += get_row_number_groups(upper_row, column)


    if (column-1) > 0 and current_line[column-1].isnumeric():
        n_numbers_around += 1

    if column < len(current_line) and current_line[column+1].isnumeric():
        n_numbers_around += 1

    if row != len(input)-1:
        lower_row = input[row+1].strip()
        n_numbers_around += get_row_number_groups(lower_row, column)

    return n_numbers_around


def compute_asterisk(row, column):

    current_line = input[row]

    upper_value = 1
    if row != 0:
        upper_row = input[row-1].strip()
        upper_value = get_row_numbers(upper_row, column)

    left_value = 1
    if (column-1) > 0 and current_line[column-1].isnumeric():
        left_index = column - 1
        while left_index > 0 and current_line[left_index].isnumeric():
            left_index -= 1
        if not current_line[left_index].isnumeric():
            left_index += 1
        left_value = int(current_line[left_index:column])

    right_value = 1
    if (column+1) < len(current_line) and current_line[column+1].isnumeric():
        right_index = column + 1
        while right_index < len(current_line) and current_line[right_index].isnumeric():
            right_index += 1
        right_value = int(current_line[column+1:right_index])

    lower_value = []
    if row != len(input)-1:
        lower_row = input[row+1].strip()
        lower_value = get_row_numbers(lower_row, column)

    return upper_value * left_value * right_value * lower_value


with open("input.txt") as f:
    input = f.readlines()

count = 0
row = 0
while row < len(input):
    current_line = input[row].strip()
    column = 0
    left_index = -1
    right_index = -1
    while column < len(current_line):
        if current_line[column] == "*":

            n_numbers_around = compute_numbers_around(row, column)

            if n_numbers_around > 1:

                count += compute_asterisk(row, column)

        column += 1
    row += 1


print(count)


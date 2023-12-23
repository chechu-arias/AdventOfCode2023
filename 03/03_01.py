

def is_valid_number(c):
    return not c.isnumeric() and c != "."

def is_valid_row(row, left_index, right_index):
    for i in range(left_index-1, right_index+1):
        if i > 0 and i < len(row):
            current_column = row[i]
            if is_valid_number(current_column):
                return True
    return False

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
        if current_line[column].isnumeric():
            left_index = column
            check_number = column
            while (check_number+1) < len(current_line) and current_line[check_number+1].isnumeric():
                check_number += 1
            right_index = check_number + 1

            if row != 0:
                upper_row = input[row-1].strip()
                if is_valid_row(upper_row, left_index, right_index):
                    count += int(current_line[left_index:right_index])
                    column = right_index +1
                    continue

            if  ((left_index-1) > 0 and is_valid_number(current_line[left_index-1])) or \
                (right_index < len(current_line) and is_valid_number(current_line[right_index])):
                count += int(current_line[left_index:right_index])
                column = right_index +1
                continue

            if row != len(input)-1:
                lower_row = input[row+1].strip()
                if is_valid_row(lower_row, left_index, right_index):
                    count += int(current_line[left_index:right_index])
                    column = right_index +1
                    continue

        column += 1
    row += 1


print(count)


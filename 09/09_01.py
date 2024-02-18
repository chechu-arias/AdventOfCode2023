
with open("./input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

res = 0
for sequence in input:
    sequence = list(map(int, sequence.split()))

    sequence_values = [sequence]
    while any(x != 0 for x in sequence_values[-1]):
        current_iteration = sequence_values[-1]
        index = 0
        while index < len(current_iteration)-1:
            diff_value = current_iteration[index+1] - current_iteration[index]
            if index == 0:
                sequence_values.append([diff_value])
            else:
                sequence_values[-1].append(diff_value)
            index += 1

    res += sum([current_sequence[-1] for current_sequence in sequence_values])
    print(sum([current_sequence[-1] for current_sequence in sequence_values]))

print(res)

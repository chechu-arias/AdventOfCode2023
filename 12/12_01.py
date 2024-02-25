
with open("./input.txt", "r") as f:
    input_data = [line.strip() for line in f.readlines()]


def find_next_question(sequence, start_pos=0):
    for index in range(start_pos, len(sequence)):
        if sequence[index] == '?':
            return index
    return -1

def stop_condition(options):
    for option in options:
        if '?' in option:
            return False
    return True

def check_question_option(sequence, values):
    values_pos = 0
    started_hashtag = False
    current_hashtag_seq = 0
    for c in sequence:
        if values_pos == len(values):
            return True
        if c == '#' and not started_hashtag:
            started_hashtag = True
            current_hashtag_seq = 1
        elif c == '#':
            current_hashtag_seq += 1
        elif c == '.' and started_hashtag and current_hashtag_seq != values[values_pos]:
            return False
        elif started_hashtag and current_hashtag_seq == values[values_pos]:
            values_pos += 1
            started_hashtag = False
            current_hashtag_seq = 0

        if c == '?':
            break

    return True


def check_option(sequence, values):
    values_pos = 0
    started_hashtag = False
    current_hashtag_seq = 0
    for index, c in enumerate(sequence):
        if c == '#' and not started_hashtag:
            started_hashtag = True
            current_hashtag_seq = 1
        elif c == '#':
            current_hashtag_seq += 1
        elif started_hashtag and current_hashtag_seq != values[values_pos]:
            return False
        elif started_hashtag and current_hashtag_seq == values[values_pos]:
            values_pos += 1
            started_hashtag = False
            current_hashtag_seq = 0
            if values_pos == len(values):
                if '#' not in sequence[index:]:
                    return True
                else:
                    return False


    if values_pos == (len(values)-1) and started_hashtag and values[values_pos] == current_hashtag_seq:
        return True

    return False


res = 0
for line in input_data:

    elements = line.split()
    sequence = elements[0]
    values = list(map(int, elements[1].split(",")))

    print(sequence, values)


    options = [sequence]
    while True:
        if stop_condition(options):
            break

        new_options = list()
        for option in options:
            index = find_next_question(option)
            for swap_option in ['.', '#']:
                if index == 0:
                    new_options.append(swap_option + option[index+1:])
                elif index == len(option):
                    print('x')
                    new_options.append(option[:index] + swap_option + option[index+1:])
                else:
                    new_options.append(option[:index] + swap_option + option[index+1:])

        options = []
        for new_sequence in new_options:
            if check_question_option(new_sequence, values):
                options.append(new_sequence)

    definitive_options = []
    for option in options:
        if check_option(option, values):
            definitive_options.append(option)

    res += len(definitive_options)

print(res)

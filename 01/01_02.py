
NUMBERS = [
"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

with open("input.txt") as f:
    input = f.readlines()

count = 0
for line in input:
    start = -1
    end = -1
    line = line.strip()
    left_words = list()
    right_words = list()
    index = 0
    while index < len(line):

        if start != -1 and end != -1:
            break

        start_char = line[index]
        end_char = line[len(line) - index - 1]

        if start_char.isnumeric() and start == -1:
            start = int(start_char) * 10
        if end_char.isnumeric() and end == -1:
            end = int(end_char)

        for index_left in range(len(left_words)):
            left_words[index_left] += start_char
        left_words.append(start_char)

        for index_right in range(len(right_words)):
            right_words[index_right] = end_char + right_words[index_right]
        right_words.append(end_char)

        for number_pos, number in enumerate(NUMBERS):
            if number in left_words and start == -1:
                start = (number_pos+1) * 10
            if number in right_words and end == -1:
                end = (number_pos+1)

        index += 1

    count += start + end

print(count)


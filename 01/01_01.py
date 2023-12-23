

with open("input.txt") as f:
    input = f.readlines()

count = 0
for line in input:
    start = -1
    end = -1
    line = line.strip()
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
        index += 1
    count += start + end

print(count)


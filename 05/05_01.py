
with open("input.txt") as f:
    input = f.readlines()

seeds = input[0].split(":")[1].strip().split()

all_mapping_ranges = list()

index = 1
while index < len(input):
    line = input[index].strip()
    if len(line) == 0:
        index += 1
        continue

    if line.endswith(":"):
        end_index = index + 1
        while end_index < len(input) and (not input[end_index].strip().endswith(":")):
            end_index += 1

        if end_index == len(input):
            end_index -= 1
        else:
            end_index -= 2

        all_mapping_ranges.append((index + 1, end_index))

    index += 1

seeds = list(map(int, seeds))

for mapping_range in all_mapping_ranges:
    start_line, end_line = mapping_range[0], mapping_range[1]
    map_tuples = list()
    map_conversions = list()

    for line_index in range(start_line, end_line+1):
        line = list(map(int, input[line_index].strip().split()))
        map_tuples.append((line[1], line[1] + line[2] - 1))
        map_conversions.append(line[0])

    for seed_index, seed in enumerate(seeds):
        for tuple_index, map_tuple in enumerate(map_tuples):
            if seed >= map_tuple[0] and seed <= map_tuple[1]:
                print(seed, map_tuple[0], map_tuple[1])
                seeds[seed_index] = seed - map_tuple[0] + map_conversions[tuple_index]

print(min(seeds))

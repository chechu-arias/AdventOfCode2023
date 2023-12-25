

with open("input.txt") as f:
    input = f.readlines()

res = 0
for line in input:
    line = line.strip()
    numbers = line.split(":")[1].split("|")
    winning_numbers = set(numbers[0].strip().split())
    current_numbers = numbers[1].strip().split()

    current_card = 0
    for number in current_numbers:
        if number in winning_numbers:
            current_card *= 2
            if not current_card:
                current_card = 1

    res += current_card

print(res)

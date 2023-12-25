

with open("input.txt") as f:
    input = f.readlines()

card_counts = {}

res = 0
for line in input:
    line = line.strip()
    elements = line.split(":")
    card_id = int(elements[0].strip().replace("Card ", ""))
    card_counts[card_id] = card_counts.get(card_id, 0) + 1
    numbers = elements[1].split("|")
    winning_numbers = set(numbers[0].strip().split())
    current_numbers = numbers[1].strip().split()

    current_card = 0
    for number in current_numbers:
        if number in winning_numbers:
            current_card += 1

    for i in range(card_id+1, card_id+current_card+1):
        card_counts[i] = card_counts.get(i, 0) + card_counts[card_id]


print(sum(card_counts.values()))

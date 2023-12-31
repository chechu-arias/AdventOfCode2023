
ORDER = [
    "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"
]

REPOKER = 6
POKER = 5
FULL = 4
TRIPLE = 3
DOUBLES = 2
DOUBLE = 1
HIGH = 0

def get_hand_type(hand):
    card_counts = dict()
    j_values = 0
    for card in hand:
        if card == "J":
            j_values += 1
            continue
        card_counts[card] = card_counts.get(card, 0) + 1

    if j_values > 0:
        max_v = 0
        max_cards = []
        for card, card_count in card_counts.items():
            if card_count > max_v:
                max_v = card_count
                max_cards = [card]
            elif card_count == max_v:
                max_cards.append(card)

        if len(max_cards) == 0:
            return REPOKER

        best_card = max_cards[0]
        if len(max_cards) == 1:
            card_counts[best_card] = card_counts[best_card] + j_values
        else:
            best_card_value = ORDER.index(best_card)
            for card in max_cards:
                value = ORDER.index(card)
                if best_card is None or value < best_card_value:
                    best_card = card
                    best_card_value = value
            card_counts[best_card] = card_counts[best_card] + j_values


    card_count_list = list(card_counts.values())
    if max(card_count_list) == 5:
        return REPOKER
    if max(card_count_list) == 4:
        return POKER
    if max(card_count_list) == 3 and min(card_count_list) == 2:
        return FULL
    if max(card_count_list) == 3:
        return TRIPLE
    if max(card_count_list) == 1:
        return HIGH

    pairs = 0
    for card, card_count in card_counts.items():
        if card_count == 2:
            pairs += 1
    if pairs == 1:
        return DOUBLE

    return DOUBLES

def has_higher_card(current, other):
    for i in range(len(current)):
        if current[i] != other[i]:
            current_index = ORDER.index(current[i])
            other_index = ORDER.index(other[i])
            if current_index > other_index:
                return False
            else:
                return True

with open("input.txt") as f:
    input = f.readlines()

ordered_types = list()
ordered_hands = list()
ordered_biddings = list()
for line in input:
    line_elements = line.strip().split()
    current_hand = line_elements[0]
    current_bid = int(line_elements[1])

    current_hand_type = get_hand_type(current_hand)

    added = False
    hand_index = 0
    while hand_index < len(ordered_hands):
        comparing_hand = ordered_hands[hand_index]
        if ordered_types[hand_index] < current_hand_type:
            added = True
            ordered_hands.insert(hand_index, current_hand)
            ordered_biddings.insert(hand_index, current_bid)
            ordered_types.insert(hand_index, current_hand_type)
            break
        elif ordered_types[hand_index] == current_hand_type and has_higher_card(current_hand, ordered_hands[hand_index]):
            added = True
            ordered_hands.insert(hand_index, current_hand)
            ordered_biddings.insert(hand_index, current_bid)
            ordered_types.insert(hand_index, current_hand_type)
            break
        hand_index += 1

    if not added:
        ordered_hands.append(current_hand)
        ordered_biddings.append(current_bid)
        ordered_types.append(current_hand_type)

ordered_hands.reverse()
ordered_biddings.reverse()

res = 0
for i in range(len(ordered_biddings)):
    res += (i+1) * ordered_biddings[i]

print(res)

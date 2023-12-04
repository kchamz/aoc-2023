import re

with open("input.txt") as file:
    content = file.read()

cards_mapping = {}
total_copies = 0

for card_num, line in enumerate(content.split("\n"), 1):
    line = line.split(":")[1].strip().split("|")

    clean_up = lambda x: set(re.sub(r"\s+", " ", x).strip().split(" "))

    winning_numbers = clean_up(line[0])
    numbers = clean_up(line[1])

    cards_mapping[card_num] = {
        "matches": len(winning_numbers & numbers),
        "copies": 1
    }

for card_num, card_info in cards_mapping.items():
    total_copies += card_info["copies"]
    for _ in range(card_info["copies"]):
        for num in range(card_num + 1, card_num + 1 + card_info["matches"]):
            cards_mapping[num]["copies"] += 1


print(total_copies)

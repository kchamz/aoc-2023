from functools import reduce
import re

with open("input.txt") as file:
    content = file.read()

total_score = 0

for line in content.split("\n"):
    line = line.split(":")[1].strip().split("|")

    clean_up = lambda x: set(re.sub(r"\s+", " ", x).strip().split(" "))

    winning_numbers = clean_up(line[0])
    numbers = clean_up(line[1])

    if matches := numbers & winning_numbers:
        score = reduce(lambda s, _: s * 2, range(len(matches) - 1), 1)
        total_score += score

print(total_score)

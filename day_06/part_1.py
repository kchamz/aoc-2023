import re
from functools import reduce

with open("input.txt") as file:
    content = file.read()

clean_up = lambda index: list(
    map(
        int,
        re.sub(r"\s+", " ", content.split("\n")[index].split(":")[1].strip()).split(
            " "
        ),
    )
)

games = []

for race in zip(clean_up(0), clean_up(1)):
    time = race[0]
    distance = race[1]

    smallest = 0
    for t in range(time):
        if t * (time - t) > distance:
            smallest = t
            break

    biggest = 0
    for t in range(time, -1, -1):
        if t * (time - t) > distance:
            biggest = t
            break

    games.append(len(range(smallest, biggest + 1)))

print(reduce(lambda x, y: x * y, games))

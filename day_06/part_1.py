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

    mapping = {x: result for x in range(time) if (result := x * (time - x)) > distance}

    games.append(len(mapping))

print(reduce(lambda x, y: x * y, games))

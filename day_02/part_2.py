import operator
from functools import reduce

with open(file="input.txt") as file:
    content = file.read()

total = 0
for game_num, line in enumerate(content.split("\n"), 1):
    rounds = line.split(":")[1].split(";")
    impossible = False

    min_bag = {}

    for r in rounds:
        cubes = {
            parts[1].lower(): int(parts[0])
            for cube in r.split(",")
            if (parts := cube.strip().split(" "))
        }

        for cube in cubes:
            if min_bag.get(cube, None) is not None:
                min_bag[cube] = max(min_bag[cube], cubes[cube])
                pass
            else:
                min_bag[cube] = cubes[cube]

    total += reduce(operator.mul, min_bag.values(), 1)

print(total)

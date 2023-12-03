import itertools
import re
from collections import defaultdict
from functools import reduce

with open("input.txt") as file:
    content = file.read()

symbol_coordinates = [
    (i.start(), line_num)
    for line_num, line in enumerate(content.split("\n"))
    for i in re.finditer(r"[^\d.]", line)
]

adjacent_coordinates = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

parts_by_symbol_coords = defaultdict(list)

for current_y_coord, line in enumerate(content.split("\n")):
    numbers_only = re.finditer(r"\d+", line)

    for number in numbers_only:
        for current_x_coord in range(*number.span()):
            for coords in adjacent_coordinates:
                if (
                    current_x_coord + coords[0],
                    current_y_coord + coords[1],
                ) in symbol_coordinates:
                    current_coords = (
                        current_x_coord + coords[0],
                        current_y_coord + coords[1],
                    )
                    parts_by_symbol_coords[current_coords].append(int(number.group(0)))
                    break
            else:
                continue
            break


print(
    sum(
        [
            reduce((lambda x, y: x * y), nums)
            for nums in parts_by_symbol_coords.values()
            if len(nums) > 1
        ]
    )
)

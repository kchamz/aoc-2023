import re

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

total = 0

for current_y_coord, line in enumerate(content.split("\n")):
    numbers_only = re.finditer(r"\d+", line)

    for number in numbers_only:
        for current_x_coord in range(*number.span()):
            for coords in adjacent_coordinates:
                if (
                    current_x_coord + coords[0],
                    current_y_coord + coords[1],
                ) in symbol_coordinates:
                    total += int(number.group(0))
                    break
            else:
                continue
            break

print(total)

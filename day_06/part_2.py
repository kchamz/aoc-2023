import re

with open("input.txt") as file:
    content = file.read()

clean_up = lambda index: int(
    re.sub(r"\s+", "", content.split("\n")[index].split(":")[1])
)

game = (clean_up(0), clean_up(1))

time = game[0]
distance = game[1]

mapping = {x: result for x in range(time) if (result := x * (time - x)) > distance}

print(len(mapping))

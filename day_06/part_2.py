import re

with open("input.txt") as file:
    content = file.read()

clean_up = lambda index: int(
    re.sub(r"\s+", "", content.split("\n")[index].split(":")[1])
)

game = (clean_up(0), clean_up(1))

time = game[0]
distance = game[1]

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

print(len(range(smallest, biggest + 1)))

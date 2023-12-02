with open(file="input.txt") as file:
    content = file.read()


bag = {"red": 12, "green": 13, "blue": 14}

total_games = []
for game_num, line in enumerate(content.split("\n"), 1):
    rounds = line.split(":")[1].split(";")
    impossible = False

    for r in rounds:
        round_bag = bag
        cubes = {
            parts[1].lower(): int(parts[0])
            for cube in r.split(",")
            if (parts := cube.strip().split(" "))
        }
        remaining = {
            key: round_bag[key] - cubes[key] for key in set(cubes) & set(round_bag)
        }
        round_bag = {**round_bag, **remaining}

        if any([v < 0 for v in round_bag.values()]):
            impossible = True
            break

    if not impossible:
        total_games.append(game_num)

print(sum(total_games))

from collections import namedtuple

with open("input.txt") as file:
    content = file.read().split("\n\n")

seeds = list(map(int, content[0].split(":")[1].strip().split(" ")))

mapping_info = namedtuple("MappingInfo", ["destination", "source", "length"])

categories = {}
for line in content[1:]:
    category = line.split(":")[0]
    mappings = [
        mapping_info(destination=int(mri[0]), source=int(mri[1]), length=int(mri[2]))
        for mapping in line.split(":")[1].strip().split("\n")
        if (mri := mapping.split(" "))
    ]
    categories[category] = mappings

mapped_seeds = []
for seed in seeds:
    new_seed = seed
    for category, mappings in categories.items():
        for mapping in mappings:
            if mapping.source <= new_seed < mapping.source + mapping.length:
                diff = new_seed - mapping.source
                mapped_num = mapping.destination + diff
                new_seed = mapped_num
                break

    mapped_seeds.append(new_seed)

print(min(mapped_seeds))

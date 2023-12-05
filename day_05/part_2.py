from collections import namedtuple

with open("input.txt") as file:
    content = file.read().split("\n\n")

seeds = list(map(int, content[0].split(":")[1].strip().split(" ")))

seeds_ranges = [range(x[0], x[0] + x[1]) for x in list(zip(seeds[::2], seeds[1::2]))]

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

for category, mappings in categories.items():
    mapped_new_seed_ranges = []
    for seed_range in seeds_ranges:
        found_mapping = False
        for mapping in sorted(mappings, key=lambda obj: obj.source):
            mapping_range = range(mapping.source, mapping.source + mapping.length)
            intersecting_range = range(
                max(mapping_range.start, seed_range.start),
                min(mapping_range.stop, seed_range.stop),
            )

            if len(intersecting_range):
                found_mapping = True
                if intersecting_range.start > seed_range.start:
                    mapped_new_seed_ranges.append(
                        range(seed_range.start, intersecting_range.start)
                    )

                if intersecting_range:
                    start_diff = intersecting_range.start - mapping.source
                    start_mapped_num = mapping.destination + start_diff

                    stop_diff = intersecting_range.stop - mapping.source
                    stop_mapped_num = mapping.destination + stop_diff

                    mapped_range = range(start_mapped_num, stop_mapped_num)
                    mapped_new_seed_ranges.append(mapped_range)

                if intersecting_range.stop < seed_range.stop:
                    seed_range = range(intersecting_range.stop, seed_range.stop)

        if not found_mapping:
            mapped_new_seed_ranges.append(seed_range)

    if mapped_new_seed_ranges:
        seeds_ranges = mapped_new_seed_ranges


print(min(seed_range.start for seed_range in seeds_ranges))

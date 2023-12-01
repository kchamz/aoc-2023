import re

with open(file="input.txt") as f:
    content = f.read()

mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

mapping.update({str(x): x for x in range(1, 10)})

pattern = re.compile(fr"(?=(\d|{'|'.join(mapping.keys())}))")
lines = [re.findall(pattern, line) for line in content.split("\n")]
total = sum(int(f"{mapping[line[0]]}{mapping[line[-1]]}") if len(line) >= 1 else 0 for line in lines)
print(total)

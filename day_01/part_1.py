import re

with open(file="input.txt") as f:
    content = f.read()

lines = [list(re.sub(r'\D', '', raw_line)) for raw_line in content.split("\n")]
total = sum(int(f"{line[0]}{line[-1]}") if len(line) >= 1 else 0 for line in lines)
print(total)

import re

with open("day3.txt", 'r') as f:
    line = f.read()

    total = 0
    valid_muls = re.findall("mul\(\d+,\d+\)", line)

    total = 0
    for mul in valid_muls:
        integers = [int(x) for x in  re.findall("\d+", mul)]
        total += integers[0] * integers[1]

    print(f"Day 3-1: {total}")



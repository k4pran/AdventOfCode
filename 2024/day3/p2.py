import re

def find_substrings(s):
    enabled = True
    substrings = []
    current_str = ""
    for i in range(len(s)):
        current_str += s[i]
        if enabled and "don't()" in current_str:
            substrings.append(current_str)
            current_str = ""
            enabled = False
        if not enabled and "do()" in current_str:
            current_str = ""
            enabled = True
    if enabled:
        substrings.append(current_str)
    return substrings


with open("day3.txt", 'r') as f:
    line = f.read()

    total = 0
    valid_muls = []
    for do_mul in find_substrings(line):
        valid_muls += re.findall("mul\(\d+,\d+\)", do_mul)

    total = 0

    for mul in valid_muls:
        integers = [int(x) for x in  re.findall("\d+", mul)]
        total += integers[0] * integers[1]

    print(f"Day 3-2: {total}")



DIAL_LIMIT = 100
START = 50

with open("day1.txt", 'r') as f:
    lines = f.read().splitlines()

    zeros = 0
    current_pos = START
    for line in lines:
        direction = 1 if line[0] == 'R' else -1
        rotations = int(line[1:])

        current_pos = (current_pos + direction * rotations) % DIAL_LIMIT
        print(current_pos)
        if current_pos == 0:
            zeros += 1

    print(f"Day 1-1: {zeros}")
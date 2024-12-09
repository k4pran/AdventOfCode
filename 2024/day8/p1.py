from collections import defaultdict

from data.grid import as_grid, is_in_grid

with open("day8.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0

    grid = as_grid(lines)

    frequency_locs = defaultdict(list)
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '.':
                continue

            frequency_locs[col].append((i, j))

    antinodes = set()
    for frequency in frequency_locs.keys():
        for loc_1 in frequency_locs[frequency]:
            for loc_2 in frequency_locs[frequency]:
                print(loc_1, loc_2)
                if loc_1 != loc_2:
                    x_dist = loc_1[0] - loc_2[0]
                    y_dist = loc_1[1] - loc_2[1]

                    antinode = (loc_1[0] + x_dist, loc_1[1] + y_dist)
                    if is_in_grid(grid, antinode):
                        antinodes.add(antinode)



    print(f"Day 8-1: {len(antinodes)}")




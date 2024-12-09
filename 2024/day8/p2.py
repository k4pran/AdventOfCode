from collections import defaultdict

from data.grid import as_grid, is_in_grid, print_grid

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
        if (len(frequency_locs[frequency]) <= 1):
            continue
        for loc_1 in frequency_locs[frequency]:
            for loc_2 in frequency_locs[frequency]:
                if loc_1 != loc_2:
                    x_dist = loc_1[0] - loc_2[0]
                    y_dist = loc_1[1] - loc_2[1]

                    antinode = (loc_1[0], loc_1[1])
                    while is_in_grid(grid, antinode):
                        antinodes.add(antinode)
                        antinode = (antinode[0] + x_dist, antinode[1] + y_dist)



    print_grid(grid, replace={k: '#' for k in antinodes})

    print(f"Day 8-2: {len(antinodes)}")




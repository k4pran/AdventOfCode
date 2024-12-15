import copy
from collections import deque, defaultdict

from data.grid import as_grid, get_adjacent, print_grid


def count_horizontal_sides(region_rows):
    sides = 0
    sorted_rows = sorted(region_rows.keys())  # Ensure rows are in order

    for row in sorted_rows:
        if len(region_rows[row]) == 1:
            pass
            # check up and down - if up != SAME PLANT TYPE then add side, if bottom not same plant type add side
            # only do count up and down once for a continuous side

    return sides


def find_region(grid, start):
    plot_type = grid[start[0]][start[1]]
    q = deque([start])
    region = [start]

    sides = 0
    counted_sides = set()
    rows = defaultdict(list)
    while q:
        loc = q.popleft()

        for adj in get_adjacent(grid, loc):
            if adj not in region and grid[adj[0]][adj[1]] == plot_type:
                q.append(adj)
                region.append(adj)


            if grid[adj[0]][adj[1]] == plot_type:
                if adj[1] not in rows[loc[0]]:
                    rows[loc[0]].append(adj[1])


    return region, (count_horizontal_sides(rows) * 2) * len(region)

def find_cost(grid):

    visited = set()
    region_coords = []
    total_cost = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in visited:
                continue
            region, cost = find_region(grid, (i, j))
            total_cost += cost
            region_coords.append(region)
            visited.update(region)

    return total_cost, region_coords

with open("day12.txt", 'r') as f:
    lines = f.read().splitlines()

    grid = as_grid(lines)

    cost = 0
    cost, regions = find_cost(grid)

    print(f"\nDay 12-2: {cost}")




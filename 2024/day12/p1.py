from collections import deque

from data.grid import as_grid, get_adjacent


def find_region(grid, start):
    plot_type = grid[start[0]][start[1]]
    q = deque([start])
    region = [start]
    perimeter = 0
    while q:
        loc = q.popleft()

        cell_perim = 4
        for adj in get_adjacent(grid, loc):
            if adj not in region and grid[adj[0]][adj[1]] == plot_type:
                q.append(adj)
                region.append(adj)

            if grid[adj[0]][adj[1]] == plot_type:
                cell_perim -= 1

        perimeter += cell_perim


    return region, perimeter * len(region)

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

    print(f"\nDay 12-1: {cost}")




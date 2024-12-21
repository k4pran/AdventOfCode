from collections import deque, defaultdict

from data.grid import as_grid, get_adjacent, print_grid


def count_horizontal_sides(region_rows):
    sides = 0
    sorted_rows = sorted(region_rows.keys())  # Ensure rows are in order

    for row in sorted_rows:
        # check up
        row_above = region_rows.get(row - 1, None)
        row_below = region_rows.get(row + 1, None)

        previous_col = None
        side_started = False
        for col in sorted(region_rows[row]):
            # top edge
            if not row_above and not side_started:
                side_started = True

            if row_above and col in row_above:
                if side_started:
                    sides += 1
                    side_started = False

            if row_above and col not in row_above:
                if not side_started:
                    side_started = True

            if previous_col and previous_col + 1 != col:
                if side_started:
                    sides += 1
                    side_started = False

            previous_col = col
        if side_started:
            sides += 1

        previous_col = None
        side_started = False
        for col in sorted(region_rows[row]):
            # bottom edge
            if not row_below and not side_started:
                side_started = True

            if row_below and col in row_below:
                if side_started:
                    sides += 1
                    side_started = False

            if row_below and col not in row_below:
                if not side_started:
                    side_started = True

            if previous_col and previous_col + 1 != col:
                if side_started:
                    sides += 1
                    side_started = False

            previous_col = col
        if side_started:
            sides += 1

    return sides


def find_region(grid, start):
    plot_type = grid[start[0]][start[1]]
    q = deque([start])
    region = [start]

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

    if len(rows) == 0 and len(region) == 1:
        return region, 4 * len(region), 4
    sides = count_horizontal_sides(rows) * 2
    return region, (sides) * len(region), sides

def find_cost(grid):

    visited = set()
    region_coords = []
    total_cost = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in visited:
                continue
            region, cost, sides = find_region(grid, (i, j))
            total_cost += cost
            print(f"region {cell} -- sides {sides} -- cost {cost}")

            region_coords.append(region)
            visited.update(region)

    return total_cost, region_coords

with open("day12.txt", 'r') as f:
    lines = f.read().splitlines()

    grid = as_grid(lines)

    cost = 0
    cost, regions = find_cost(grid)

    print(f"\nDay 12-2: {cost}")




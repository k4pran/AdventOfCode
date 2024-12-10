from collections import deque

from data.grid import as_grid, print_grid, add_2d_padding


def find_trailheaders(grid):
    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0':
                trailheads.append((i, j))
    return trailheads


def get_valid_adjacent(grid, pos):
    old_c = int(grid[pos[0]][pos[1]])
    adjacents = []
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_pos = (pos[0] + x, pos[1] + y)

        new_c = grid[new_pos[0]][new_pos[1]]
        if new_c.isdigit() and int(new_c) - old_c == 1:
            adjacents.append(new_pos)
    return adjacents


def dfs(grid, start, needle) -> bool:
    stack = deque([start])

    destination_count = 0
    found_already = set()
    while stack:
        node = stack.pop()
        print(node)

        for adj in get_valid_adjacent(grid, node):
            if grid[adj[0]][adj[1]] == needle and f"{grid}, {adj}" not in found_already:
                destination_count += 1
                found_already.add(f"{grid}, {adj}")
            if adj not in stack:
                stack.append(adj)

    return destination_count


with open("day10.txt", 'r') as f:
    lines = f.read().splitlines()

    grid = as_grid(lines)
    grid = add_2d_padding(grid, '-', 1)
    print_grid(grid)

    trailheads = find_trailheaders(grid)
    print(f"TRAILHEADS - {trailheads}")

    trailhead_scores = 0
    for trailhead in trailheads:
        trailhead_scores += dfs(grid, trailhead, "9")


    print(f"\nDay 10-1: {trailhead_scores}")




from collections import defaultdict

from data.grid import add_2d_padding

guard_moves = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

change_dirs = {
    0: '^',
    1: '>',
    2: 'v',
    3: '<'
}


def as_grid(lines):
    return [[col for col in row] for row in lines]


def find_starting_pos(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] in guard_moves:
                return i, j


with open("day6.txt", 'r') as f:
    lines = f.read().splitlines()

    grid = as_grid(lines)
    grid = add_2d_padding(grid, padding_char='!', layers=2)

    exited = False
    visited = set()
    guard = find_starting_pos(grid)
    direction = 0
    while not exited:
        visited.add(guard)
        move = guard_moves[grid[guard[0]][guard[1]]]
        next_pos = guard[0] + move[0], guard[1] + move[1]
        if grid[next_pos[0]][next_pos[1]] == '!':
            exited = True
            break
        if grid[next_pos[0]][next_pos[1]] == '#':
            direction = (direction + 1) % 4
            grid[guard[0]][guard[1]] = change_dirs[direction]
        else:
            grid[guard[0]][guard[1]] = '.'
            guard = next_pos
            grid[guard[0]][guard[1]] = change_dirs[direction]

        print(guard)

    print(f"Day 6-1: {len(visited)}")



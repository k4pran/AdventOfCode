from collections import defaultdict, deque
import copy

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


def find_starting_pos(guard_grid):
    for i, row in enumerate(guard_grid):
        for j, col in enumerate(row):
            if guard_grid[i][j] in guard_moves:
                return i, j


def perform_simulation(guard_grid):
    visited = set()
    guard = find_starting_pos(guard_grid)
    direction = 0
    looping = False
    loop_check = set()
    while True:
        if (guard, direction) in loop_check:
            return visited, True
        loop_check.add((guard, direction))
        visited.add(guard)

        move = guard_moves[guard_grid[guard[0]][guard[1]]]
        next_pos = guard[0] + move[0], guard[1] + move[1]
        if guard_grid[next_pos[0]][next_pos[1]] == '!':
            break
        if guard_grid[next_pos[0]][next_pos[1]] == '#':
            direction = (direction + 1) % 4
            guard_grid[guard[0]][guard[1]] = change_dirs[direction]
        else:
            if guard in loop_check and next_pos in loop_check:
                return visited, True
            guard_grid[guard[0]][guard[1]] = '.'
            guard = next_pos
            guard_grid[guard[0]][guard[1]] = change_dirs[direction]

    return visited, looping


with open("day6.txt", 'r') as f:
    lines = f.read().splitlines()

    grid = as_grid(lines)
    grid = add_2d_padding(grid, padding_char='!', layers=2)

    visited, _ = perform_simulation(copy.deepcopy(grid))

    loops = 0

    for node in visited:
        if node == find_starting_pos(grid):
            continue
        updated_grid = copy.deepcopy(grid)
        updated_grid[node[0]][node[1]] = '#'
        _, looping = perform_simulation(updated_grid)
        if looping:
            loops += 1


    print(f"Day 6-2: {loops}")

    # 748 - nope
    # 947 - nope
    # 1916 - ?



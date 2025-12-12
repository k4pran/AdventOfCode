from data.grid import get_down, get_left, get_right, as_grid, print_grid

START = 'S'
SPLITTER = '^'

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == START:
                return i, j

def execute_beams(grid, beam_pos, memo):
    next_pos = get_down(grid, beam_pos)
    if not next_pos:
        return 1

    cell = grid[next_pos[0]][next_pos[1]]

    if cell != SPLITTER:
        return execute_beams(grid, next_pos, memo)

    if next_pos in memo:
        return memo[next_pos]

    left = get_left(grid, next_pos)
    right = get_right(grid, next_pos)

    l = execute_beams(grid, left, memo)
    r = execute_beams(grid, right, memo)

    memo[next_pos] = l + r
    return memo[next_pos]


with open("day7.txt", 'r') as f:

    block = f.read().splitlines()

    grid = as_grid(block)

    start = find_start(grid)

    split_count = execute_beams(grid, start, dict())

    print(f"Day 7-2: {split_count}")

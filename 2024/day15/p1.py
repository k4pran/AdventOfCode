from data.grid import as_grid, print_grid, search_grid, search_all_grid

actions_map = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}


def move_boxes(grid, pos, action):
    new_pos = pos
    while True:
        x, y = actions_map[action]
        new_pos = new_pos[0] + x, new_pos[1] + y
        if grid[new_pos[0]][new_pos[1]] == '#':
            return False
        if grid[new_pos[0]][new_pos[1]] == '.':
            break

    while pos != new_pos:
        pos = pos[0] + x, pos[1] + y
        grid[pos[0]][pos[1]] = 'O'
    return True

def move(grid, pos, action):
    x, y = actions_map[action]
    new_pos = pos[0] + x, pos[1] + y

    if grid[new_pos[0]][new_pos[1]] == '#':
        return pos
    elif grid[new_pos[0]][new_pos[1]] == '.':
        grid[new_pos[0]][new_pos[1]] = '@'
        grid[pos[0]][pos[1]] = '.'
        return new_pos
    elif grid[new_pos[0]][new_pos[1]] == 'O':
        moved = move_boxes(grid, new_pos, action)
        if moved:
            grid[new_pos[0]][new_pos[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            return new_pos
    return pos

with open("day15.txt", 'r') as f:
    grid, actions = f.read().split("\n\n")
    grid = grid.splitlines()
    grid = as_grid(grid)

    pos = search_grid(grid, '@')

    for action in actions.replace("\n", ""):
        pos = move(grid, pos, action)
        print_grid(grid)
        print("\n")

    boxes = search_all_grid(grid, 'O')
    total = 0
    for box in boxes:
        total += 100 * box[0] + box[1]

    print(f"\nDay 15-1: {total}")

from data.grid import as_grid, print_grid, search_grid, search_all_grid

actions_map = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

box_cells = {'[', ']'}
horizontal_actions = {'<', '>'}

def make_grid(lines):
    grid = []
    for row in lines:
        row_list = []
        for col in row:
            if col == '#':
                row_list.append('#')
                row_list.append('#')
            if col == 'O':
                row_list.append('[')
                row_list.append(']')
            if col == '.':
                row_list.append('.')
                row_list.append('.')
            if col == '@':
                row_list.append('@')
                row_list.append('.')
        grid.append(row_list)
    return grid


def move_boxes_horizontally(grid, pos, action):
    new_pos = pos
    x, y = actions_map[action]
    while True:
        new_pos = new_pos[0] + x, new_pos[1] + y
        cell = grid[new_pos[0]][new_pos[1]]
        if cell == '#':
            return False
        elif cell == '.':
            break
        # elif cell in box_cells:
        #     new_pos = new_pos[0] + x, new_pos[1] + y

    while pos != new_pos:
        pos = pos[0] + x, pos[1] + y
        grid[pos[0]][pos[1]] = '[' if action == '>' else ']'

        pos = pos[0] + x, pos[1] + y
        grid[pos[0]][pos[1]] = ']' if action == '>' else '['
    return True


def move_boxes_vertically(grid, pos, action):
    current_positions_to_move = [pos]
    old_positions = []
    x, y = actions_map[action]
    while True:
        updated_pos = []
        for np in current_positions_to_move:
            np = np[0] + x, np[1] + y
            cell = grid[np[0]][np[1]]
            if cell == '#':
                return False
            if cell == '.':
                continue
            if cell == ']':
                if np not in updated_pos:
                    updated_pos.append(np)
                    updated_pos.append((np[0], np[1] - 1))
            if cell == '[':
                if np not in updated_pos:
                    updated_pos.append(np)
                    updated_pos.append((np[0], np[1] + 1))
        if updated_pos:
            current_positions_to_move = updated_pos
            old_positions.extend(updated_pos)

        else:
            break


    for pos in reversed(old_positions):
        cell = grid[pos[0]][pos[1]]
        new_pos = pos[0] + x, pos[1] + y
        grid[new_pos[0]][new_pos[1]] = cell
        grid[pos[0]][pos[1]] = '.'
    return True

def move(grid, pos, action):
    x, y = actions_map[action]
    new_pos = pos[0] + x, pos[1] + y

    cell = grid[new_pos[0]][new_pos[1]]
    if cell == '#':
        return pos
    elif cell == '.':
        grid[new_pos[0]][new_pos[1]] = '@'
        grid[pos[0]][pos[1]] = '.'
        return new_pos
    elif cell in box_cells and action in horizontal_actions:
        moved = move_boxes_horizontally(grid, new_pos, action)
        if moved:
            grid[new_pos[0]][new_pos[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            return new_pos
    elif cell in box_cells:
        moved = move_boxes_vertically(grid, pos, action)
        if moved:
            grid[new_pos[0]][new_pos[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            return new_pos
    return pos

with open("day15.txt", 'r') as f:
    grid, actions = f.read().split("\n\n")
    grid = grid.splitlines()
    grid = make_grid(grid)

    pos = search_grid(grid, '@')
    print_grid(grid)

    i = 0
    for action in actions.replace("\n", ""):
        pos = move(grid, pos, action)
        # print(f"Move {i}")
        # print_grid(grid)
        i += 1

    boxes = search_all_grid(grid, '[')
    total = 0
    for box in boxes:
        total += 100 * box[0] + box[1]

    print(f"\nDay 15-2: {total}")

def as_grid(lines):
    return [[col for col in row] for row in lines]


def search_grid(grid, target):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == target:
                return (i, j)
    return None

def search_all_grid(grid, target):
    found = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == target:
                found.append((i, j))
    return found

def print_grid_from_coords(coords, width, height):
    grid = [['.' for _ in range(width)] for _ in range(height)]

    for x, y in coords:
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = '#'

    for row in grid:
        print(''.join(row))


def get_up(grid, loc):
    row, col = loc
    if row > 0 and col < len(grid[row - 1]):
        return (row - 1, col)
    return None


def get_down(grid, loc):
    row, col = loc
    if row + 1 < len(grid) and col < len(grid[row + 1]):
        return (row + 1, col)
    return None


def get_left(grid, loc):
    row, col = loc
    if col > 0:
        return (row, col - 1)
    return None


def get_right(grid, loc):
    row, col = loc
    if col + 1 < len(grid[row]):
        return (row, col + 1)
    return None

def get_adjacent(grid, loc):
    adj = []

    for neighbor in (
        get_up(grid, loc),
        get_down(grid, loc),
        get_left(grid, loc),
        get_right(grid, loc),
    ):
        if neighbor is not None:
            adj.append(neighbor)

    return adj

def get_up_left(grid, loc):
    row, col = loc
    if row > 0 and col > 0:
        return (row - 1, col - 1)
    return None


def get_up_right(grid, loc):
    row, col = loc
    if row > 0 and col + 1 < len(grid[row - 1]):
        return (row - 1, col + 1)
    return None


def get_down_left(grid, loc):
    row, col = loc
    if row + 1 < len(grid) and col > 0:
        return (row + 1, col - 1)
    return None


def get_down_right(grid, loc):
    row, col = loc
    if row + 1 < len(grid) and col + 1 < len(grid[row + 1]):
        return (row + 1, col + 1)
    return None

def get_diagonals(grid, loc):
    diag = []

    for neighbor in (
        get_up_left(grid, loc),
        get_up_right(grid, loc),
        get_down_left(grid, loc),
        get_down_right(grid, loc),
    ):
        if neighbor is not None:
            diag.append(neighbor)

    return diag

def get_adj_and_diagonal(grid, loc):
    return get_adjacent(grid, loc) + get_diagonals(grid, loc)

def print_grid(grid, replace=None):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if replace is not None and (i, j) in replace:
                print(replace[(i, j)], end="")
            else:
                print(col, end="")
        print()

def replace_cells(grid, positions, replace_char):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if positions is not None and (i, j) in positions:
                grid[i][j] = replace_char

def add_2d_padding(grid, padding_char, layers=1):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    new_rows = rows + 2 * layers
    new_cols = cols + 2 * layers

    safety_grid = [[padding_char] * new_cols for _ in range(new_rows)]

    for i in range(rows):
        for col in range(cols):
            safety_grid[i + layers][col + layers] = grid[i][col]

    return safety_grid


def slice_right_segment(grid, row, col, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    return grid[row][col:col + nb_cells]

def slice_left_segment(grid, row, col, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    return grid[row][col:max(col - nb_cells, -1):-1] or [grid[row][col]]

def slice_down_segment(grid, col, row, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    return [row[col] for row in grid[row:row + nb_cells]]

def slice_up_segment(grid, row, col, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    nb_cells = min(nb_cells, row + 1)
    return [grid[row - n][col] for n in range(nb_cells)]


def slice_up_right_segment(grid, row, col, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    nb_cells = min(nb_cells, len(grid[0]) - col, row + 1)
    return [grid[row - n][col + n] for n in range(nb_cells)]


def slice_up_left_segment(grid, row, col, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    nb_cells = min(nb_cells, col + 1, row + 1)
    return [grid[row - n][col - n] for n in range(nb_cells)]

def slice_down_right_segment(grid, row, col, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    nb_cells = min(nb_cells, len(grid) - row, len(grid[0]) - col)  # Fix here: include the current row
    return [grid[row + n][col + n] for n in range(nb_cells)]

def slice_down_left_segment(grid, row, col, nb_cells):
    if not grid or nb_cells <= 0:
        return None
    nb_cells = min(nb_cells, len(grid) - row, col + 1)
    return [grid[row + n][col - n] for n in range(nb_cells)]
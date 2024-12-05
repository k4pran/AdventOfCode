

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
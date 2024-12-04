import re


def add_safety_zone(grid, layers=1):
    # Get the dimensions of the original grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Create a new grid with extra layers of zeros
    new_rows = rows + 2 * layers
    new_cols = cols + 2 * layers

    # Initialize the new grid with zeros
    safety_grid = [["0"] * new_cols for _ in range(new_rows)]

    # Copy the original grid into the center of the new grid
    for i in range(rows):
        for j in range(cols):
            safety_grid[i + layers][j + layers] = grid[i][j]

    return safety_grid

def as_grid(lines):
    return [[col for col in row] for row in lines]

def find_xmas(grid, i, j):
    count = 0
    valid_strs = {"MAS", "SAM"}
    valid_x = False

    #NE
    if "".join([grid[i - n + 1][j + n - 1] for n in range(3)]) in valid_strs and \
       "".join([grid[i + n - 1][j + n - 1] for n in range(3)]) in valid_strs:
        count += 1

    #NW
    if "".join([grid[i - n][j - n] for n in range(4)]) in valid_strs:
        count += 1

    return count


with open("day4.txt", 'r') as f:
    lines = f.read().splitlines()

    grid = add_safety_zone(as_grid(lines), 4)

    total = 0
    for i in range(4, len(grid) - 4):
        for j in range(4, len(grid[i]) - 4):
            if grid[i][j] == 'A':
                total += find_xmas(grid, i, j)

    print(f"Day 4-2: {total}")



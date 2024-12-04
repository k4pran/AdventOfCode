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
    valid_strs = {"XMAS", "SAMX"}

    # right
    if "".join(grid[i][j:j+4]) in valid_strs:
        count += 1

    # left
    if "".join(grid[i][j - 3:j + 1]) in valid_strs:
        count += 1

    #down
    if "".join([row[j] for row in grid[i:i + 4]]) in valid_strs:
        count += 1

    #up
    if "".join([row[j] for row in grid[i - 3:i + 1]]) in valid_strs:
        count += 1

    #NE
    if "".join([grid[i + n][j + n] for n in range(4)]) in valid_strs:
        count += 1

    #NW
    if "".join([grid[i - n][j - n] for n in range(4)]) in valid_strs:
        count += 1

    #SE
    if "".join([grid[i - n][j + n] for n in range(4)]) in valid_strs:
        count += 1

    #SW
    if "".join([grid[i + n][j - n] for n in range(4)]) in valid_strs:
        count += 1

    return count


with open("day4.txt", 'r') as f:
    lines = f.read().splitlines()

    grid = add_safety_zone(as_grid(lines), 4)

    total = 0
    for i in range(4, len(grid) - 4):
        for j in range(4, len(grid[i]) - 4):
            if grid[i][j] == 'X':
                total += find_xmas(grid, i, j)

    print(f"Day 4-1: {total}")



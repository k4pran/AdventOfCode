from data.grid import add_2d_padding


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

    grid = add_2d_padding(as_grid(lines), '0', 4)

    total = 0
    for i in range(4, len(grid) - 4):
        for j in range(4, len(grid[i]) - 4):
            if grid[i][j] == 'X':
                total += find_xmas(grid, i, j)

    print(f"Day 4-1: {total}")



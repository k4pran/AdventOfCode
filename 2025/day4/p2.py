from data.grid import as_grid, print_grid, get_adj_and_diagonal, replace_cells

with open("day4.txt", 'r') as f:

    lines = f.read().splitlines()

    total = 0
    grid = as_grid(lines)
    print_grid(grid)

    while True:
        positions = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '@':
                    continue
                neighbours = get_adj_and_diagonal(grid, (i, j))
                toilet_rolls = 0
                for n in neighbours:
                    if grid[n[0]][n[1]] == '@':
                        toilet_rolls += 1


                if toilet_rolls < 4:
                    total += 1
                    positions[(i, j)] = 'X'

        if len(positions) == 0:
            break

        replace_cells(grid, positions, ".")

    print("\n\n")
    print_grid(grid, positions)

    print(f"Day 4-1: {total}")
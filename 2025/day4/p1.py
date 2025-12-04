from data.grid import as_grid, print_grid, get_adj_and_diagonal, print_grid_from_coords

with open("day4.txt", 'r') as f:

    lines = f.read().splitlines()

    total = 0
    grid = as_grid(lines)
    print_grid(grid)

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


    print("\n\n")
    print_grid(grid, positions)

    print(f"Day 4-1: {total}")
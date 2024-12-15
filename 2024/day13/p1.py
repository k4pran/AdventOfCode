from data.grid import as_grid, get_adjacent


def find_combinations(x, y, z):
    combinations = []

    for a in range(z // x + 1):
        remainder = z - a * x
        if remainder >= 0 and remainder % y == 0:
            b = remainder // y
            combinations.append((a, b))

    return combinations


def find_cheapest(machine):

    x_combos = find_combinations(machine[0][0], machine[1][0], machine[2][0])
    y_combos = find_combinations(machine[0][1], machine[1][1], machine[2][1])

    intersection = set(x_combos).intersection(y_combos)

    cheapest = None
    for intersection in intersection:
        if not cheapest:
            coins = (intersection[0] * 3) + intersection[1]
            cheapest = (intersection, coins)
        else:
            coins = (intersection[0] * 3) + intersection[1]
            if coins < cheapest[1]:
                cheapest = (intersection, coins)

    return cheapest[1] if cheapest else 0

with open("day13.txt", 'r') as f:
    blocks = f.read().split("\n\n")

    machines = []
    for block in blocks:
        block = block.split("\n")
        button_a = [int(a) for a in block[0].split(": ")[-1].replace("X", "").replace("Y", "").replace("+", "").split(", ")]
        button_b = [int(a) for a in block[1].split(": ")[-1].replace("X", "").replace("Y", "").replace("+", "").split(", ")]
        prize = [int(a) for a in block[2].split(": ")[-1].replace("X", "").replace("Y", "").replace("=", "").split(", ")]

        machines.append((button_a, button_b, prize))

    coins = 0
    for machine in machines:
        coins += find_cheapest(machine)



    grid = as_grid(blocks)

    print(f"\nDay 13-1: {coins}")




import numpy as np

def find_combinations(x, y, z):
    combinations = []

    for a in range(z // x + 1):
        remainder = z - a * x
        if remainder >= 0 and remainder % y == 0:
            b = remainder // y
            combinations.append((a, b))

    return combinations


def find_cheapest(machine):
    mat_a = np.array([[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]])
    mat_b = np.array([10000000000000 + machine[2][0], 10000000000000 + machine[2][1]])

    solution = np.linalg.solve(mat_a, mat_b)

    a, b = solution
    a, b = round(a), round(b)

    px_approx = a * mat_a[0][0] + b * mat_a[0][1]
    py_approx = a * mat_a[1][0] + b * mat_a[1][1]

    # Validate the rounging makes sense and didn't create an invalid solution
    if px_approx == mat_b[0] and py_approx == mat_b[1] and a >= 0 and b >= 0:
        coins = (a * 3) + b
        print(f"Coins required: {coins}")
        return coins
    else:
        return 0




# Parse input file
with open("day13.txt", 'r') as f:
    blocks = f.read().split("\n\n")

    machines = []
    for block in blocks:
        block = block.split("\n")
        button_a = [int(a) for a in block[0].split(": ")[-1].replace("X", "").replace("Y", "").replace("+", "").split(", ")]
        button_b = [int(a) for a in block[1].split(": ")[-1].replace("X", "").replace("Y", "").replace("+", "").split(", ")]
        prize = [int(a) for a in block[2].split(": ")[-1].replace("X", "").replace("Y", "").replace("=", "").split(", ")]

        machines.append((button_a, button_b, prize))

    # Calculate total coins for all machines
    coins = 0
    for machine in machines:
        machine_coins = find_cheapest(machine)
        if machine_coins:
            coins += machine_coins

    print(f"\nDay 13-2: {coins}")

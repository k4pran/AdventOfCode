def max_voltage(bank):
    bat_1 = (-1, 0)
    for i, bat in enumerate(bank[:-1]):
        bat = int(bat)
        if bat > bat_1[1]:
            bat_1 = (i, bat)

    bat_2 = (-1, 0)
    for i, bat in enumerate(bank[bat_1[0] + 1:]):
        bat = int(bat)
        if bat > bat_2[1]:
            bat_2 = (i, bat)


    return (bat_1[1], bat_2[1])

with open("day3.txt", 'r') as f:
    lines = f.read().splitlines()

    joltage = 0

    for line in lines:
        bat_1, bat_2 = max_voltage(line)
        total = int(str(bat_1) + str(bat_2))
        print(total)
        joltage += total

    print(f"Day 3-1: {joltage}")
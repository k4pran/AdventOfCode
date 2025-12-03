NB_BATS = 12
def max_voltage(bank):

    bats = []
    current_index = last_index = 0
    for b in range(NB_BATS):
        bat_1 = 0
        for i, bat in enumerate(bank[current_index:len(bank) - NB_BATS + b + 1]):
            bat = int(bat)
            if bat > bat_1:
                current_index = i + 1 + last_index
                bat_1 = bat

        bats.append(bat_1)
        last_index = current_index

    return bats

with open("day3.txt", 'r') as f:
    lines = f.read().splitlines()

    joltage = 0
    for line in lines:
        bats = max_voltage(line)
        s = ""
        for bat in bats:
            s += str(bat)
        total = int(s)
        joltage += total

    print(f"Day 3-2: {joltage}")
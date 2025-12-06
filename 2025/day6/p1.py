with open("day6.txt", 'r') as f:

    lines = f.read().splitlines()

    rows = []
    for line in lines:
        numbers = [i for i in map(int, line.split())]
        rows.append(numbers)

    nb_cols = len(rows[0])

    operation_line = lines[-1].split()
    totals = []
    for col in range(nb_cols):
        op = operation_line[col]
        col_total = rows[0][col]
        for row in rows[1:]:
            if op == '*':
                col_total *= row[col]
            elif op == '+':
                col_total += row[col]
            else:
                raise ValueError
        totals.append(col_total)


    print(f"Day 6-1: {sum(totals)}")
from collections import defaultdict
from functools import reduce

with open("day6.txt", 'r') as f:

    lines = f.read().splitlines()

    cols = defaultdict(list)
    for line in lines[:-1]:
        for c_index, col in enumerate(line):
            cols[c_index].append(col)

    operation_line = lines[-1].split()

    totals = []
    current_op_idx = 0

    op = operation_line[current_op_idx]
    current_col_total = 0 if op == '+' else 1
    for row, col in cols.items():

        if all(x == ' ' for x in col):
            current_op_idx += 1
            op = operation_line[current_op_idx]
            print(current_col_total)
            totals.append(current_col_total)
            current_col_total = 0 if op == '+' else 1
            continue

        nb = reduce(lambda x, y: x + y, [x for x in col if x != ' '])
        if op == '*':
            current_col_total *= int(nb)
        elif op == '+':
            current_col_total += int(nb)


    totals.append(current_col_total)


    print(f"Day 6-2: {sum(totals)}")
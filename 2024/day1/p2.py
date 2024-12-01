with open("day1.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    l1, l2 = [], []
    tabular = dict()
    for line in lines:
        first, second = map(int, line.split())
        l1.append(first)
        if second not in tabular:
            tabular[second] = 0
        tabular[second] += 1

    for m in l1:
        total += m * tabular.get(m, 0)

    print(f"Day 1-2: {total}")
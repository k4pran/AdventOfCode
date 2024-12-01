with open("day1.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    l1, l2 = [], []
    for line in lines:
        first, second = map(int, line.split())
        l1.append(first)
        l2.append(second)
    l1 = sorted(l1)
    l2 = sorted(l2)

    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])

    print(f"Day 1-1: {total}")
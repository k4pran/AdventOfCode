with open("day5.txt", 'r') as f:

    lines = f.read().split("\n\n")

    raw_ranges = lines[0].splitlines()
    ids = map(int, lines[1].splitlines())

    ranges = []
    for r in raw_ranges:
        ranges.append([i for i in map(int, r.split("-"))])

    ranges = sorted(ranges, key=lambda x: x[0])

    flattened_ranges = []
    flattened_ranges.append(ranges[0])
    last_range = ranges[0]

    for range in ranges:
        if range[1] <= range[0]:
            print(range)

    for r in ranges[1:]:
        if r[0] <= last_range[1]:
            last_range[1] = max(last_range[1], r[1])
            continue
        flattened_ranges.append(r)
        last_range = r

    total = 0

    print(flattened_ranges)
    for range in flattened_ranges:
        total += range[1] - range[0] + 1 ## inclusive so add the 1

    print(f"Day 5-2: {total}")
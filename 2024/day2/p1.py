def is_safe(report):
    sign = 1 if report[0] < report[1] else -1
    allowed_range = {i * sign for i in range(1, 4)}
    for i in range(1, len(report)):
        if not (report[i] - report[i - 1] in allowed_range):
            return False

    return True

with open("day2.txt", 'r') as f:
    lines = f.read().splitlines()

    reports = [list(map(int, line.split())) for line in lines]

    safe_nb = 0
    for report in reports:
        if is_safe(report):
            safe_nb += 1

    print(f"Day 2-1: {safe_nb}")



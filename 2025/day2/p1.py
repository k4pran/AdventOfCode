DIAL_LIMIT = 100
START = 50

with open("day2.txt", 'r') as f:
    lines = f.read().split(",")

    invalid_codes = 0
    for line in lines:
        start, end = map(int, line.split("-"))

        for i in range(start, end + 1):
            s = str(i)
            if (len(s) % 2 == 1):
                continue

            l = len(s)
            l_half = l // 2
            if s[:l_half] == s[l_half:]:
                invalid_codes += i


    print(f"Day 2-1: {invalid_codes}")
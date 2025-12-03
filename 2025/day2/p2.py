from sympy import divisors

with open("day2.txt", 'r') as f:
    lines = f.read().split(",")

    invalid_codes = 0
    for line in lines:
        start, end = map(int, line.split("-"))

        for i in range(start, end + 1):

            s = str(i)
            if i < 10:
                continue
            if len(set(c for c in s)) == 1:
                invalid_codes += i
                continue

            l = len(s)

            factors = divisors(len(s))


            for factor in factors:
                if factor == 1 or factor == l:
                    continue

                part_len = l // factor
                prev_chunk = None
                chunks = []
                for j in range(0, l, part_len):
                    chunks.append(s[j:j + part_len])

                if len(chunks) > 1 and len(set(chunks)) == 1:
                    invalid_codes += i
                    break


    print(f"Day 2-2: {invalid_codes}")
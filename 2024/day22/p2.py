from collections import deque, defaultdict


def calc_secret_number(secret):
    new_secret = secret * 64
    new_secret = new_secret ^ secret
    new_secret %= 16777216

    nb_divided = new_secret // 32
    new_secret = nb_divided ^ new_secret
    new_secret %= 16777216

    nb_mulled = new_secret * 2048
    new_secret = nb_mulled ^ new_secret
    new_secret %= 16777216


    return new_secret

with open("day22.txt", 'r') as f:
    lines = f.read().splitlines()

    iterations = 2000
    memo = defaultdict(int)
    best_sequence = (None, 0)
    for line in lines:
        window = deque(maxlen=4)
        secret_number = int(line)
        visited = set()
        for i in range(iterations):
            new_secret_number = calc_secret_number(secret_number)

            prev_dig = secret_number % 10
            next_dig = new_secret_number % 10

            window.append(next_dig - prev_dig)

            if len(window) == 4:
                sequence = tuple(window)
                if sequence not in visited:
                    memo[sequence] += next_dig
                    if memo[sequence] > best_sequence[1]:
                        best_sequence = (sequence, memo[sequence])
                    visited.add(sequence)

            secret_number = new_secret_number

    print(f"BEST SEQUENCE {best_sequence}")

    print(f"\nDay 22-2: {best_sequence[1]}")

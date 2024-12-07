import time
from collections import deque


def is_even(num):
    return num % 2 == 0

def get_combos(nums, result):
    possibilities = deque(nums[:1])
    for num in nums[1:]:
        for _ in range(len(possibilities)):
            possibility = possibilities.popleft()
            if possibility > result:
                continue
            possibilities.append(possibility * num)
            possibilities.append(possibility + num)
            possibilities.append(int(str(possibility) + str(num)))

    return list(possibilities)


with open("day7.txt", 'r') as f:
    start = time.time()
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        result, nums = line.split(": ")
        result = int(result)
        nums = [int(x) for x in nums.split(" ")]
        if not is_even(result) and all([is_even(x) for x in nums]):
            continue
        if result in get_combos(nums, result):
            total += result


    print(f"Day 7-2: {total}")
    end = time.time()
    print(f"Time taken: {end - start}")
    # 1.6867587566375732 seconds :(



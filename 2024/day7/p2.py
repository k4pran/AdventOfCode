import time
operators = ('+', '*')
memo = dict()

def is_even(num):
    return num % 2 == 0


def get_combos(nums, result):
    possibilities = list(nums[:1])
    for num in nums[1:]:
        updated = []
        for possibility in possibilities:
            if possibility > result:
                continue
            r1 = possibility * num
            r2 = possibility + num
            r3 = int(str(possibility) + str(num))
            updated.append(r1)
            updated.append(r2)
            updated.append(r3)

        possibilities = updated
    return possibilities


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
    # 1.6867587566375732 :(



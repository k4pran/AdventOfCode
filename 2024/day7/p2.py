from collections import defaultdict

operators = ('+', '*')
memo = dict()

def is_even(num):
    return num % 2 == 0


def get_combos(nums):
    possibilities = list(nums[:1])
    for num in nums[1:]:
        updated = []
        for possibility in possibilities:
            r1 = possibility * num
            r2 = possibility + num
            r3 = int(str(possibility) + str(num))
            updated.append(r1)
            updated.append(r2)
            updated.append(r3)

        possibilities = updated
    print(possibilities)
    return possibilities


with open("day7.txt", 'r') as f:
    lines = f.read().splitlines()

    total = 0
    for line in lines:
        result, nums = line.split(": ")
        result = int(result)
        nums = [int(x) for x in nums.split(" ")]
        if not is_even(result) and all([is_even(x) for x in nums]):
            continue
        if result in get_combos(nums):
            total += result


    print(f"Day 7-2: {total}")



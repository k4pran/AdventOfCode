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
        # todo why this not work? oh because 5 + 5 * 5 = even
        # odd is 2k + 1
        # (2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1) = 2k where k = a + b + a -> always even +. that's why it failed!
        # (2a + 1) * (2b + 1) = 4ab + 2a + 2b + 1 = 2(2ab + a + b) + 1 = 2k + 1 where k = 2ab + a + b -> always odd
        # if is_even(result) and all([not is_even(x) for x in nums]):
        #     continue

        # I think below make sense - 4 * 4 + 2 = even. x = 2k.
        # 2a + 2b = 2(a + b) = 2k where k = (a + b) -> always even
        # 2a * 2b = 2(a * b) = 2k where k = (a * b) -> always even
        if not is_even(result) and all([is_even(x) for x in nums]):
            continue
        if result in get_combos(nums):
            total += result


    print(f"Day 7-1: {total}")

    # nope - 1985078235904 - too low (I think)
    # nope - 1985268803998 - too high
    # 1985268524462 - YUP



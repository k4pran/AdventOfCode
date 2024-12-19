from collections import defaultdict


def can_form_design(design, towels, memo, matches=0):
    if design == "":
        return matches + 1

    # wow finally memoization was faster
    if design in memo:
        return memo[design]

    for towel in towels:
        if design.startswith(towel):
            match_count = can_form_design(design[len(towel):], towels, memo)
            if match_count >= 0:
                memo[design] = memo.get(design, 0) + match_count

    return memo[design]

def count_possible_designs(towels, designs):
    memo = defaultdict(int)
    possible_count = 0

    for design in designs:
        matches = can_form_design(design, towels, memo)
        possible_count += matches

    return possible_count


with open("day19.txt", 'r') as f:
    blocks = f.read().split("\n\n")

    available_towels = blocks[0].split(", ")
    designs = blocks[1].splitlines()

    total = count_possible_designs(available_towels, designs)

    print(f"\nDay 19-2: {total}")

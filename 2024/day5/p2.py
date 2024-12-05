from collections import defaultdict
from functools import cmp_to_key


def is_in_order(page, page_rules, came_before):
    if page not in page_rules:
        return True
    rules = page_rules[page]
    for rule in rules:
        if rule in came_before:
            return False
    return True

def sort_func(x, y):
    global page_rules
    if x not in page_rules and y not in page_rules:
        return 0

    if y in page_rules[x]:
        return -1
    if x in page_rules[y]:
        return 1
    return 0


with open("day5.txt", 'r') as f:
    block = f.read()

    orderings, pages = block.split("\n\n")

    page_rules = defaultdict(set)
    for order in orderings.splitlines():
        left, right = order.split("|")
        page_rules[left].add(right)


    middles = []
    pages = pages.splitlines()
    pages = [p.split(",") for p in pages]



    for page_group in pages:
        came_before = set()
        valid = True
        for page in page_group:
            if not is_in_order(page, page_rules, came_before):
                valid = False
                break
            came_before.add(page)

        if not valid:
            sorted_group = sorted(page_group, key=cmp_to_key(sort_func))
            middles.append(int(sorted_group[int((len(sorted_group) - 1) / 2)]))


    total = sum(middles)
    print(f"Day 5-2: {total}")
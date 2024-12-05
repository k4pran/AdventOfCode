from collections import defaultdict

def is_in_order(page, page_rules, came_before):
    if page not in page_rules:
        return True
    rules = page_rules[page]
    for rule in rules:
        if rule in came_before:
            return False
    return True


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

        if valid:
            middles.append(int(page_group[int((len(page_group) - 1) / 2)]))

    total = sum(middles)
    print(f"Day 5-1: {total}")



def can_form_design(design, towels):
    if design == "":
        return True

    for towel in towels:
        if design.startswith(towel):
            if can_form_design(design[len(towel):], towels):
                return True

    return False

def count_possible_designs(towels, designs):
    possible_count = 0

    for design in designs:
        if can_form_design(design, towels):
            possible_count += 1

    return possible_count


with open("day19.txt", 'r') as f:
    blocks = f.read().split("\n\n")

    available_towels = blocks[0].split(", ")
    designs = blocks[1].splitlines()

    total = count_possible_designs(available_towels, designs)

    print(f"\nDay 19-1: {total}")

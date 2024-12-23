from collections import defaultdict

with open("day23.txt", 'r') as f:
    lines = f.read().splitlines()

    result = 0

    connections = defaultdict(list)

    for connection in lines:
        comp_1, comp_2 = connection.split("-")

        connections[comp_1].append(comp_2)
        connections[comp_2].append(comp_1)

    computer_groups = []
    for connection in lines:
        comp_1, comp_2 = connection.split("-")
        for key in connections.keys():
            if key == comp_1 or key == comp_2:
                continue
            if comp_1 in connections[key] and comp_2 in connections[key]:
                result += 1
                computer_groups.append((comp_1, comp_2, key))


    computer_groups = set({tuple(sorted(t)) for t in computer_groups})

    result = 0
    for group in computer_groups:
        for computer in group:
            if computer.startswith("t"):
                result += 1
                break

    print(f"\nDay 23-1: {result}")

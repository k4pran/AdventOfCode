from collections import defaultdict, deque


def find_clique(graph, start):
    stack = deque([start])
    visited = set()
    visited.add(start)

    while stack:
        node = stack.pop()

        for adj in graph.get(node, []):
            if adj not in visited:
                if all(adj in graph[n] for n in visited):
                    stack.append(adj)
                    visited.add(adj)

    return visited


with open("day23.txt", 'r') as f:
    lines = f.read().splitlines()

    result = 0

    connections = defaultdict(set)

    for connection in lines:
        comp_1, comp_2 = connection.split("-")

        connections[comp_1].add(comp_2)
        connections[comp_2].add(comp_1)

    largest_network = set()
    for key in connections:
        nodes = find_clique(connections, key)
        if len(nodes) > len(largest_network):
            largest_network = nodes

    print(largest_network)
    print(f"\nDay 23-2: {",".join([c for c in sorted(largest_network)])}")

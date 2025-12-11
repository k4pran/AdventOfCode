from collections import deque


def find_paths(inp, graph):

    q = deque()
    for o in graph[inp]:
        q.appendleft(o)
    visited = set()
    visited.add(inp)

    paths = 0
    while q:
        node = q.popleft()

        visited.add(node)

        for output in graph.get(node, []):
            if output == "out":
                paths += 1
                break

            q.appendleft(output)

    return paths


with open("day11.txt", 'r') as f:

    lines = f.read().splitlines()

    devices = dict()
    yous = []
    for line in lines:
        inp, outs = line.split(": ")
        outs = outs.split(" ")
        devices[inp] = outs

    print(devices)

    path_count = find_paths("you", devices)


    print(f"Day 11-1: {path_count}")
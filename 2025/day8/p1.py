import math


def straight_line_dist(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 +(p2[1] - p1[1])**2 +(p2[2] - p1[2])**2)

class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


with open("day8.txt", 'r') as f:

    lines = f.read().splitlines()

    coords = []
    for line in lines:
        coords.append(tuple(map(int, line.split(","))))

    pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dist = straight_line_dist(coords[i], coords[j])
            pairs.append((dist, coords[i], coords[j]))

    pairs.sort(key=lambda x: x[0])
    ordered_pairs = pairs[:1000]

    circuits = []
    for dist, p1, p2 in ordered_pairs:

        join_indices = []
        for i, c in enumerate(circuits):
            if p1 in c:
                join_indices.append(i)
            if p2 in c:
                join_indices.append(i)

        if len(join_indices) == 0:
            s = set()
            s.add(p1)
            s.add(p2)
            circuits.append(s)

        if len(join_indices) == 1:
            circuits[join_indices[0]].add(p1)
            circuits[join_indices[0]].add(p2)

        elif len(join_indices) == 2:
            i1, i2 = join_indices[0], join_indices[1]

            if i1 == i2:
                circuits[i1].add(p1)
                circuits[i1].add(p2)
            else:
                circuits[i1].update(circuits[i2])
                circuits[i1].add(p1)
                circuits[i1].add(p2)
                circuits.pop(i2)

    top3 = sorted(circuits, key=lambda x: len(x), reverse=True)[:3]

    result = len(top3[0]) * len(top3[1]) * len(top3[2])

    print(f"Day 8-1: {result}")
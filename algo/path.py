import math
import heapq
from typing import Dict


def dijkstra(graph: Dict, start):
    visited = set()
    distances = {n: math.inf for n in graph.keys()}
    distances[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        _, node = heapq.heappop(pq)
        visited.add(node)

        for adj in graph[node]:
            weight = graph[node][adj]
            if distances[node] + weight < distances[adj]:
                distances[adj] = distances[node] + weight

            if adj not in visited and adj not in pq:
                heapq.heappush(pq, (distances[adj], adj))

    return distances


if __name__ == "__main__":
    graph = {
        'X': {'Y': 7, 'Z': 5},
        'Y': {'X': 7, 'Z': 2, 'W': 3},
        'Z': {'X': 5, 'Y': 2, 'W': 6},
        'W': {'Y': 3, 'Z': 6, 'V': 1},
        'V': {'W': 1}
    }
    start_node = 'X'

    distances = dijkstra(graph, start_node)
    print(f"Distances from {start_node}: {distances}")
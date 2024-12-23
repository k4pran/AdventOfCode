from collections import deque
from collections.abc import Callable
from typing import Any, Iterable, Dict, List, Set


def bfs(haystack: Dict, start, needle) -> bool:
    q = deque([start])
    visited = set()
    visited.add(start)

    while q:
        node = q.popleft()
        if node == needle:
            return True

        visited.add(node)

        for adj in haystack.get(node, []):
            if adj not in visited and adj not in q:
                q.append(adj)

    return False


def bfs_with_adj_func(haystack: Iterable[Any], start, needle, adj_func: Callable[[Any, Iterable[Any]], Iterable[Any]]) -> bool:
    q = deque([start])
    visited = set()
    visited.add(start)

    while q:
        node = q.popleft()
        if node == needle:
            return True

        visited.add(node)

        for adj in adj_func(node, haystack):
            if adj not in visited and adj not in q:
                q.append(adj)

    return False


def dfs(haystack: Dict[Any, List[Any]], start, needle) -> bool:
    stack = deque([start])
    visited = set()
    visited.add(start)

    while stack:
        node = stack.pop()
        if node == needle:
            return True

        visited.add(node)

        for adj in haystack.get(node, []):
            if adj not in visited and adj not in stack:
                stack.append(adj)

    return False


def dfs_track_paths(grid, start, end, adj_func: Callable[[Any, Iterable[Any]], Iterable[Any]]):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == end:
            return True, path

        if node in visited:
            continue
        visited.add(node)

        for adj in adj_func(grid, node):
            if adj not in visited:
                stack.append((adj, path + [adj]))

    return False, []


def dfs_recursive(haystack: Dict[Any, List[Any]], start, needle, visited: Set[Any] = None) -> bool:
    if visited is None:
        visited = set()

    visited.add(start)

    if start == needle:
        return True

    for adj in haystack.get(start, []):
        if adj not in visited:
            if dfs_recursive(haystack, adj, needle, visited):
                return True
    return False


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
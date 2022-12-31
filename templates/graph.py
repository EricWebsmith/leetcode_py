from typing import Any, Dict, List, Set


def get_edges(k: int, from_tos: List[List[int]]) -> Dict[int, Set[int]]:
    edges = {i+1: set() for i in range(k)}
    for from_, to_ in from_tos:
        edges[from_].add(to_)

    return edges


def get_bidirectional_edges(vetices: List, from_tos: List[List]) -> Dict[Any, Set]:
    edges = {v: set() for v in vetices}
    for from_, to_ in from_tos:
        edges[from_].add(to_)
        edges[to_].add(from_)

    return edges


def top_sort(edges: Dict[int, Set[int]]) -> List[int]:
    stack = []
    visiting = set()
    visited = set()

    cyclic = False

    def dfs(v: int):
        nonlocal cyclic
        if cyclic:
            return

        if v in visited:
            return
        if v in visiting:
            cyclic = True
            return

        if len(edges[v]) == 0:
            stack.append(v)
        else:
            visiting.add(v)
            for child in edges[v]:
                dfs(child)
            stack.append(v)
            visiting.remove(v)

        visited.add(v)

    for v in edges:
        dfs(v)

    if cyclic:
        return []

    stack.reverse()

    return stack

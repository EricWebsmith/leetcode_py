import unittest
from typing import Dict, List, Set


def get_edges(k: int, from_tos: List[List[int]]) -> Dict[int, Set[int]]:
    edges = {i + 1: set() for i in range(k)}
    for from_, to_ in from_tos:
        edges[from_].add(to_)

    return edges


def top_sort(edges: Dict[int, Set[int]]) -> List[int]:
    stack: list = []
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


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowEdges = get_edges(k, rowConditions)
        rows = top_sort(rowEdges)
        rowDict = {v: i for i, v in enumerate(rows)}
        if len(rows) == 0:
            return []

        colEdges = get_edges(k, colConditions)
        cols = top_sort(colEdges)
        colDict = {v: i for i, v in enumerate(cols)}

        if len(cols) == 0:
            return []

        mat = [[0] * k for i in range(k)]
        for i in range(k):
            mat[rowDict[i + 1]][colDict[i + 1]] = i + 1

        return mat


def test(
    testObj: unittest.TestCase,
    k: int,
    rowConditions: List[List[int]],
    colConditions: List[List[int]],
    expected: int,
) -> None:

    so = Solution()
    actual = so.buildMatrix(k, rowConditions, colConditions)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            3,
            [[1, 2], [3, 2]],
            [[2, 1], [3, 2]],
            [[3, 0, 0], [0, 0, 1], [0, 2, 0]],
        )

    def test_2(self):
        test(self, 3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]], [])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 823 ms, faster than 100.00%
Memory Usage: 23.9 MB, less than 100.00%
"""

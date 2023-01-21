import unittest
from typing import Dict, List, Set


def get_edges(k: int, from_tos: List[List[int]]) -> Dict[int, Set[int]]:
    edges: dict = {i: set() for i in range(k)}
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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = get_edges(numCourses, prerequisites)
        order = top_sort(edges)
        order.reverse()
        return order


def test(
    testObj: unittest.TestCase,
    numCourses: int,
    prerequisites: List[List[int]],
    expected: int,
) -> None:

    so = Solution()
    actual = so.findOrder(numCourses, prerequisites)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 2, [[1, 0]], [0, 1])

    def test_2(self):
        test(self, 4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3])

    def test_3(self):
        test(self, 1, [], [0])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 109 ms, faster than 89.96%
Memory Usage: 18.1 MB, less than 5.09%
"""

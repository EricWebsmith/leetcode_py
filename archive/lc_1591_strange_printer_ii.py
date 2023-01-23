import unittest
from dataclasses import dataclass
from typing import Dict, List, Set


def detect_circle(edges: Dict[int, Set[int]]) -> List[int]:
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
            pass
        else:
            visiting.add(v)
            for child in edges[v]:
                dfs(child)
            visiting.remove(v)

        visited.add(v)

    for v in edges:
        dfs(v)

    return cyclic


@dataclass
class Rectangle:
    top: int
    bottom: int
    left: int
    right: int


class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        r_dict: Dict[int, Rectangle] = dict()
        for r in range(m):
            for c in range(n):
                if not grid[r][c] in r_dict:
                    r_dict[grid[r][c]] = Rectangle(r, r, c, c)
                rec = r_dict[grid[r][c]]
                rec.top = min(rec.top, r)
                rec.bottom = max(rec.bottom, r)
                rec.left = min(rec.left, c)
                rec.right = max(rec.right, c)

        depend_dict = {color: set() for color in r_dict}
        for color, rec in r_dict.items():
            for r in range(rec.top, rec.bottom + 1):
                for c in range(rec.left, rec.right + 1):
                    if grid[r][c] != color:
                        depend_dict[color].add(grid[r][c])

        return not detect_circle(depend_dict)


def test(testObj: unittest.TestCase, targetGrid: List[List[int]], expected: bool) -> None:

    so = Solution()

    actual = so.isPrintable(targetGrid)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]], True)

    def test_2(self):
        test(self, [[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]], True)

    def test_3(self):
        test(self, [[1, 2, 1], [2, 1, 2], [1, 2, 1]], False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 569 ms, faster than 70.63%
Memory Usage: 16.4 MB, less than 11.90%
"""

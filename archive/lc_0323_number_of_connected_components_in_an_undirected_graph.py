import unittest
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> int:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1

        if px > py:
            self.p[px] = py
        else:
            self.p[py] = px
        self.e += 1
        return 0


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)

        g = [dsu.find(i) for i in range(n)]
        return len(set(g))


def test(testObj: unittest.TestCase, n: int, edges: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.countComponents(n, edges)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 5, [[0, 1], [1, 2], [3, 4]], 2)

    def test_2(self):
        test(self, 5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 106 ms, faster than 92.97%
Memory Usage: 15.4 MB, less than 67.93%
"""

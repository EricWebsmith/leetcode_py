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

    def merge(self, x: int, y: int) -> int:
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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU(n)
        connections.sort(key=lambda x: x[2])
        ans = 0
        for connection in connections:
            p0 = dsu.find(connection[0] - 1)
            p1 = dsu.find(connection[1] - 1)
            if p0 != p1:
                dsu.merge(connection[0] - 1, connection[1] - 1)
                ans += connection[2]
            if dsu.e == n - 1:
                return ans
        return -1


def test(
    testObj: unittest.TestCase, n: int, connections: List[List[int]], expected: int
) -> None:

    so = Solution()

    actual = so.minimumCost(n, connections)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]], 6)

    def test_2(self):
        test(self, 4, [[1, 2, 3], [3, 4, 4]], -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 641 ms, faster than 96.67%
Memory Usage: 19.7 MB, less than 96.16%
"""

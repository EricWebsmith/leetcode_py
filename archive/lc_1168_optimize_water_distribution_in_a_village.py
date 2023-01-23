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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        n = n + 1
        # connect to well
        for i in range(1, n):
            pipes.append([0, i, wells[i - 1]])

        pipes.sort(key=lambda x: x[2])
        dsu = DSU(n)
        ans = 0
        for pipe in pipes:
            p0 = dsu.find(pipe[0])
            p1 = dsu.find(pipe[1])
            if p0 != p1:
                dsu.merge(p0, p1)
                ans += pipe[2]
                if dsu.e == n - 1:
                    return ans
        return -1


def test(
    testObj: unittest.TestCase,
    n: int,
    wells: List[int],
    pipes: List[List[int]],
    expected: int,
) -> None:

    so = Solution()

    actual = so.minCostToSupplyWater(n, wells, pipes)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]], 3)

    def test_2(self):
        test(self, 2, [1, 1], [[1, 2, 1], [1, 2, 2]], 2)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 477 ms, faster than 99.48%
Memory Usage: 21.3 MB, less than 30.18%
"""

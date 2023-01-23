from functools import cache
import unittest
from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        def cost(i, j):
            return abs(locations[i] - locations[j])

        @cache
        def dfs(i: int, f: int):
            if f < abs(cost(i, finish)):
                return 0

            return (sum([dfs(j, f - cost(i, j)) for j in range(n) if i != j]) + (i == finish)) % 1_000_000_007

        return dfs(start, fuel) % 1_000_000_007


def test(
    testObj: unittest.TestCase,
    locations: List[int],
    start: int,
    finish: int,
    fuel: int,
    expected: int,
) -> None:

    so = Solution()
    actual = so.countRoutes(locations, start, finish, fuel)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [2, 3, 6, 8, 4], 1, 3, 5, 4)

    def test_2(self):
        test(self, [4, 3, 1], 1, 0, 6, 5)

    def test_3(self):
        test(self, [5, 2, 1], 0, 2, 3, 0)

    def test_4(self):
        test(self, [1, 2, 3], 0, 2, 40, 615088286)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
3037 ms
Beats
82.9%
"""

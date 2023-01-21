import unittest
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [0] * n

        dp[n - 1] = 1 if dungeon[m - 1][n - 1] > 0 else 1 - dungeon[m - 1][n - 1]

        for c in range(n - 2, -1, -1):
            dp[c] = max(1, dp[c + 1] - dungeon[m - 1][c])

        for r in range(m - 2, -1, -1):
            new_dp = [0] * n
            new_dp[n - 1] = max(1, dp[n - 1] - dungeon[r][n - 1])
            for c in range(n - 2, -1, -1):
                down = max(1, dp[c] - dungeon[r][c])
                right = max(1, new_dp[c + 1] - dungeon[r][c])
                best = min(down, right)
                new_dp[c] = max(1, best)

            dp = new_dp

        return dp[0]


def test(testObj: unittest.TestCase, dungeon: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.calculateMinimumHP(dungeon)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7)

    def test_2(self):
        test(self, [[0]], 1)

    def test_3(self):
        test(self, [[-2, 1, 3], [5, 10, 1], [10, 30, 5]], 3)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 75 ms, faster than 96.78%
Memory Usage: 15.1 MB, less than 55.23%
"""

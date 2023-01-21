import unittest
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * k for _ in range(n)]

        # r == 0
        s = 0
        for c in range(n):
            s += grid[0][c]
            s %= k
            dp[c][s] += 1

        # r = 1 to m
        first_s = grid[0][0]
        for r in range(1, m):
            first_s += grid[r][0]
            first_s %= k

            new_dp = [[0] * k for _ in range(n)]
            new_dp[0][first_s % k] = 1

            s = first_s
            for c in range(1, n):
                for i in range(k):
                    new_dp[c][i] = (dp[c][i] + new_dp[c - 1][i]) % 1_000_000_007
                kk = grid[r][c] % k
                new_dp[c] = new_dp[c][k - kk :] + new_dp[c][: k - kk]

            dp = new_dp
        return dp[-1][0]


def test(
    testObj: unittest.TestCase, grid: List[List[int]], k: int, expected: int
) -> None:
    so = Solution()
    actual = so.numberOfPaths(grid, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3, 2)

    def test_2(self):
        test(self, [[0, 0]], 5, 1)

    def test_3(self):
        test(self, [[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1, 10)

    def test_4(self):
        test(self, [[1], [5], [3], [7], [3], [2], [3], [5]], 29, 1)


if __name__ == "__main__":
    unittest.main()

"""
2141ms, 100%
"""

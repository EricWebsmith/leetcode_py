import unittest
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        m = k
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * n for i in range(m + 1)]

        for r in range(1, m + 1):
            max_profit = -prices[0]
            for c in range(1, n):
                dp[r][c] = max(dp[r][c - 1], prices[c] + max_profit)
                max_profit = max(max_profit, dp[r - 1][c] - prices[c])
            if dp[r][-1] == dp[r - 1][-1]:
                return dp[r][-1]
        return dp[-1][-1]


def test(testObj: unittest.TestCase, k: int, prices: List[int], expected: int) -> None:

    so = Solution()
    actual = so.maxProfit(k, prices)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 2, [2, 4, 1], 2)

    def test_2(self):
        test(self, 2, [3, 2, 6, 5, 0, 3], 7)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 99 ms, faster than 94.55%
Memory Usage: 15.3 MB, less than 65.66%
"""

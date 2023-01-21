import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowest = prices[0]
        profit = 0
        for i in range(1, n):
            profit = max(profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])

        return profit


def test(testObj: unittest.TestCase, prices: List[int], expected: int) -> None:
    so = Solution()
    actual = so.maxProfit(prices)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [7, 1, 5, 3, 6, 4], 5)

    def test_2(self):
        test(self, [7, 6, 4, 3, 1], 0)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1170 ms
Beats
86.43%
"""

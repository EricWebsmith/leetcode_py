import unittest
from functools import cache
from typing import List


class Solution:
    def __init__(self) -> None:
        self.nums: list = []
        self.n = 0

    @cache
    def dfs(self, i: int, target: int) -> int:
        if i == self.n - 1:
            count = 0
            if self.nums[i] == target:
                count += 1
            if -self.nums[i] == target:
                count += 1
            return count

        return self.dfs(i + 1, target - self.nums[i]) + self.dfs(i + 1, target + self.nums[i])

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.n = len(nums)
        return self.dfs(0, target)


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected: int) -> None:

    so = Solution()
    actual = so.findTargetSumWays(nums, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 1, 1, 1, 1], 3, 5)

    def test_2(self):
        test(self, [1], 1, 1)

    def test_3(self):
        test(self, [1, 0], 1, 2)

    def test_4(self):
        test(
            self,
            [6, 20, 22, 38, 11, 15, 22, 30, 0, 17, 34, 29, 7, 42, 46, 49, 30, 7, 14, 5],
            28,
            6738,
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 934 ms, faster than 8.92%
Memory Usage: 73.4 MB, less than 8.55%
"""

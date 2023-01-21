import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        moving_sum = nums[0]
        max_sum = moving_sum
        for i in range(1, len(nums)):
            if moving_sum <= 0:
                moving_sum = nums[i]
            else:
                moving_sum += nums[i]
            max_sum = max(max_sum, moving_sum)

        return max_sum


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()

    actual = so.maxSubArray(nums)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)

    def test_2(self):
        test(self, [1], 1)

    def test_3(self):
        test(self, [5, 4, -1, 7, 8], 23)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1213 ms
Beats
61.97%
"""

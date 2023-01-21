import unittest
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        moving_sum = [0]
        for num in nums:
            moving_sum.append(moving_sum[-1] + num)

        min_diff = 100000
        ans = 0
        for i in range(n):
            left = moving_sum[i + 1] // (i + 1)
            right = 0
            if i < n - 1:
                right = (moving_sum[-1] - moving_sum[i + 1]) // (n - i - 1)
            diff = abs(left - right)
            if diff < min_diff:
                min_diff = diff
                ans = i

        return ans


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()
    actual = so.minimumAverageDifference(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [2, 5, 3, 9, 5, 3], 3)

    def test_2(self):
        test(self, [0], 0)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1479 ms
Beats
77%
"""

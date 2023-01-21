import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            ans = max(ans, min(height[right], height[left]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans


def test(testObj: unittest.TestCase, height: List[int], expected: int) -> None:

    so = Solution()

    actual = so.maxArea(height)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 8, 6, 2, 5, 4, 8, 3, 7], 49)

    def test_2(self):
        test(self, [1, 1], 1)

    def test_3(self):
        test(self, [1, 2, 4, 3], 4)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
770 ms
Beats
94.30%
"""

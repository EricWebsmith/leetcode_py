import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]
        ans = 0
        while left < right:
            if left_max <= right_max:
                left += 1
                ans += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
            else:
                right -= 1
                ans += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
        return ans


def test(testObj: unittest.TestCase, height: List[int], expected: int) -> None:
    so = Solution()
    actual = so.trap(height)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)

    def test_2(self):
        test(self, [4, 2, 0, 3, 2, 5], 9)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
141 ms
Beats
89.22%
"""

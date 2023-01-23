import unittest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 1_000_000_000
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target - s) < abs(diff):
                    diff = target - s
                if s < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                break
        return target - diff


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected: int) -> None:
    so = Solution()
    actual = so.threeSumClosest(nums, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [-1, 2, 1, -4], 1, 2)

    def test_2(self):
        test(self, [0, 0, 0], 1, 0)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
788 ms
Beats
93.2%
"""

import unittest
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        right = n - 1
        while nums[left] < 0 and nums[right] > 0:
            if nums[right] == -nums[left]:
                return nums[right]
            elif nums[right] > -nums[left]:
                right -= 1
            else:
                left += 1

        return -1


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:
    so = Solution()
    actual = so.findMaxK(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [-1, 2, -3, 3], 3)

    def test_2(self):
        test(self, [-1, 10, 6, 7, -7, 1], 7)

    def test_3(self):
        test(self, [-10, 8, 6, 7, -2, -3], -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
159 ms
Beats
100%
"""

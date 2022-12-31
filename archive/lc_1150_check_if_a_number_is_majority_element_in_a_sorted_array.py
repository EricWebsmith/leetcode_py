import unittest
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n % 2 == 0:
            left = nums[n//2-1]
            right = nums[n//2]
            if left != right:
                return False

        candidate = nums[n//2]
        if candidate != target:
            return False
        c = bisect_right(nums, candidate) - bisect_left(nums, candidate)
        return c > n//2


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected: int) -> None:

    so = Solution()
    actual = so.isMajorityElement(nums, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [2, 4, 5, 5, 5, 5, 5, 6, 6],  5, True)

    def test_2(self):
        test(self,   [10, 100, 101, 101],  101, False)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 40 ms, faster than 92.86%
Memory Usage: 14 MB, less than 82.74%
'''

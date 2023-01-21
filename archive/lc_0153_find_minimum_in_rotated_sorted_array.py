import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = bisect_right(nums, x=-nums[0], key=lambda x: -x) % len(nums)
        return nums[index]


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()
    actual = so.findMin(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 4, 5, 1, 2], 1)

    def test_2(self):
        test(self, [4, 5, 6, 7, 0, 1, 2], 0)

    def test_3(self):
        test(self, [11, 13, 15, 17], 11)

    def test_4(self):
        test(self, [11], 11)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
50 ms
Beats
82.71%
"""

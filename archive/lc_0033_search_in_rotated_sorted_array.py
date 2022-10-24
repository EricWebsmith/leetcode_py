import unittest
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        index = bisect_right(nums, x=-nums[0], key=lambda x: -x) % n
        if index > 0:
            index_left = bisect_left(nums, target, lo=0, hi=index-1)
            if index_left < n and nums[index_left] == target:
                return index_left

        index_right = bisect_left(nums, target, lo=index)
        if index_right < n and nums[index_right] == target:
            return index_right

        return -1


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected: int) -> None:

    so = Solution()

    actual = so.search(nums, target)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [4, 5, 6, 7, 0, 1, 2],  0, 4)

    def test_2(self):
        test(self,   [4, 5, 6, 7, 0, 1, 2],  3, -1)

    def test_3(self):
        test(self,   [1],  0, -1)

    def test_4(self):
        test(self,   [1, 2, 3],  2, 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
41 ms
Beats
96.43%
'''

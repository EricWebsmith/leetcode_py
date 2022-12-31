import unittest
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window = sum(nums)
        cur = 0

        for i in range(window):
            if nums[i] == 1:
                cur += 1

        max_ones = cur
        for i in range(window, n+window):
            if nums[i % n] == 1:
                cur += 1
            if nums[i-window] == 1:
                cur -= 1
            max_ones = max(max_ones, cur)

        return window - max_ones


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()
    actual = so.minSwaps(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [0, 1, 0, 1, 1, 0, 0], 1)

    def test_2(self):
        test(self,   [0, 1, 1, 1, 0, 0, 1, 1, 0], 2)

    def test_3(self):
        test(self,   [1, 1, 0, 0, 1], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1367 ms, faster than 73.44%
Memory Usage: 17.8 MB, less than 82.81%
'''

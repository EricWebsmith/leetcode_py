import unittest
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        s = sum(nums)

        left_sum = 0
        for i in range(n):
            if left_sum * 2 + nums[i] == s:
                return i
            left_sum += nums[i]
        return -1


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:
    so = Solution()
    actual = so.pivotIndex(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 7, 3, 6, 5, 6], 3)

    def test_2(self):
        test(self,   [1, 2, 3], -1)

    def test_3(self):
        test(self,   [2, 1, -1], 0)

    def test_4(self):
        test(self,   [2], 0)

    def test_5(self):
        test(self,   [-1, -1, -1, -1, -1, 0], 2)


if __name__ == '__main__':
    unittest.main()

'''
184ms, 82.35%
'''

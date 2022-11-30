import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for i in range(n+1):
            s ^= i

        for num in nums:
            s ^= num

        return s


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:
    so = Solution()
    actual = so.missingNumber(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 0, 1], 2)

    def test_2(self):
        test(self,   [0, 1], 2)

    def test_3(self):
        test(self,   [9, 6, 4, 2, 3, 5, 7, 0, 1], 8)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
149 ms
Beats
87.16%
'''

import unittest
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[0]
        m = nums[0]
        for i in range(1, n):
            s += nums[i]
            a = s // (i+1)
            if s % (i+1) > 0:
                a += 1
            m = max(m, a)

        return m


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:
    so = Solution()
    actual = so.minimizeArrayValue(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 7, 1, 6], 5)

    def test_2(self):
        test(self,   [10, 1], 10)

    def test_3(self):
        test(self,   [13, 13, 20, 0, 8, 9, 9], 16)

    def test_5(self):
        test(self,   [1, 5, 5, 5], 4)

    def test_6(self):
        test(self,   [3, 4, 4, 4], 4)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
2237 ms
Beats
60%
'''

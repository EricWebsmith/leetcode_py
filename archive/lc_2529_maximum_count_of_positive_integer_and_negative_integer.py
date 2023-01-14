import unittest
from bisect import bisect_left, bisect_right


class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n = len(nums)
        first_zero = bisect_left(nums, x=0)
        first_one = bisect_right(nums, x=0)
        negative = first_zero
        positive = n - first_one
        return max(negative, positive)


def test(testObj: unittest.TestCase, nums: list[int], expected: int) -> None:
    so = Solution()
    actual = so.maximumCount(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [-2, -1, -1, 1, 2, 3], 3)

    def test_2(self):
        test(self,   [-3, -2, -1, 0, 0, 1, 2], 3)

    def test_3(self):
        test(self,   [5, 20, 66, 1314], 4)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
123 ms
Beats
87.78%
'''

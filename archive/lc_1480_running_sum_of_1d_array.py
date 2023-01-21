import unittest
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


def test(testObj: unittest.TestCase, nums: List[int], expected: List[int]) -> None:
    so = Solution()
    actual = so.runningSum(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4], [1, 3, 6, 10])

    def test_2(self):
        test(self, [1, 1, 1, 1, 1], [1, 2, 3, 4, 5])

    def test_3(self):
        test(self, [3, 1, 2, 10, 1], [3, 4, 6, 16, 17])


if __name__ == "__main__":
    unittest.main()

"""
65ms, 62.44%
"""

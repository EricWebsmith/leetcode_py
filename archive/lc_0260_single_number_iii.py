import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & -bitmask

        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


def test(testObj: unittest.TestCase, nums: List[int], expected: List[int]) -> None:
    so = Solution()
    actual = so.singleNumber(nums)
    actual.sort()
    expected.sort()
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 1, 3, 2, 5], [3, 5])

    def test_2(self):
        test(self, [-1, 0], [-1, 0])

    def test_3(self):
        test(self, [0, 1], [1, 0])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 54 ms, faster than 99.25%
Memory Usage: 15.8 MB, less than 48.17%
"""

import unittest
from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left = 0
        right = max(ribbons)

        while left < right:
            mid = (left + right + 1) >> 1
            c = 0
            for r in ribbons:
                c += r // mid

            if c >= k:
                left = mid
            else:
                right = mid - 1

        return left


def test(testObj: unittest.TestCase, ribbons: List[int], k: int, expected: int) -> None:

    so = Solution()

    actual = so.maxLength(ribbons, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [9, 7, 5], 3, 5)

    def test_2(self):
        test(self, [7, 5, 9], 4, 4)

    def test_3(self):
        test(self, [5, 7, 9], 22, 0)

    def test_4(self):
        test(self, [9], 3, 3)

    def test_5(self):
        test(self, [9, 9], 3, 4)

    def test_6(self):
        test(self, [9, 9, 9], 3, 9)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 2113 ms, faster than 61.22%
Memory Usage: 28 MB, less than 45.05%
"""

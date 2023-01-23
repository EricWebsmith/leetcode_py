import unittest
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        total = 0
        for d, a in shift:
            if d == 0:
                total += a
            else:
                total -= a

        total = total % n

        return s[total:] + s[0:total]


def test(testObj: unittest.TestCase, s: str, shift: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.stringShift(s, shift)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "abc", [[0, 1], [1, 2]], "cab")

    def test_2(self):
        test(self, "abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]], "efgabcd")


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 32 ms, faster than 95.89%
Memory Usage: 13.9 MB, less than 72.78%
"""


import unittest
from math import sqrt
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res: list = []
        cur: list[int] = []

        def backtrack(start, x):
            if cur:
                res.append(cur + [x])
            for factor in range(start, int(sqrt(x))+1):
                if x % factor == 0:
                    cur.append(factor)
                    backtrack(factor, x//factor)
                    cur.pop()

        backtrack(2, n)
        return res


def test(testObj: unittest.TestCase, n: int, expected: list[list[int]]) -> None:

    so = Solution()
    actual = so.getFactors(n)
    actual.sort()
    expected.sort()
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,   1, [])

    def test_2(self):
        test(self,   12, [[2, 6], [3, 4], [2, 2, 3]])

    def test_3(self):
        test(self,   37, [])


if __name__ == '__main__':
    unittest.main()

"""
Runtime: 130 ms, faster than 69.92%
Memory Usage: 15 MB, less than 52.72%
"""

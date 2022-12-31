import unittest
from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])

        rows = [0] * m
        cols = [0] * n
        for r in range(m):
            for c in range(n):
                if picture[r][c] == 'B':
                    rows[r] += 1
                    cols[c] += 1

        ans = 0
        for r in range(m):
            for c in range(n):
                if picture[r][c] == 'B' and rows[r] == 1 and cols[c] == 1:
                    ans += 1

        return ans


def test(testObj: unittest.TestCase, picture: List[List[str]], expected: int) -> None:

    so = Solution()

    actual = so.findLonelyPixel(picture)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]], 3)

    def test_2(self):
        test(self,   [["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]], 0)


if __name__ == '__main__':
    unittest.main()

'''
452ms, 98.8%
'''

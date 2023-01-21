import unittest
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        x = points[0][0]
        w = 0
        for i in range(len(points)):
            w = max(w, points[i][0] - x)
            x = points[i][0]

        return w


def test(testObj: unittest.TestCase, points: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.maxWidthOfVerticalArea(points)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[8, 7], [9, 9], [7, 4], [9, 7]], 1)

    def test_2(self):
        test(self, [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]], 3)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 1001 ms, faster than 82.76%
Memory Usage: 54.9 MB, less than 18.94%
"""

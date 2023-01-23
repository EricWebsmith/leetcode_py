import unittest
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort()
        for i in range(1, n):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


def test(testObj: unittest.TestCase, intervals: List[List[int]], expected: bool) -> None:
    so = Solution()
    actual = so.canAttendMeetings(intervals)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[0, 30], [5, 10], [15, 20]], False)

    def test_2(self):
        test(self, [[7, 10], [2, 4]], True)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
100 ms
Beats
80.55%
"""

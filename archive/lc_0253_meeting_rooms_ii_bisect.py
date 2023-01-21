import unittest
from bisect import insort_left
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        going_on: List[int] = []
        max_meetings = 1
        for start, end in intervals:
            while going_on and going_on[-1] <= start:
                going_on.pop()

            insort_left(going_on, x=end, key=lambda x: -x)
            max_meetings = max(max_meetings, len(going_on))

        return max_meetings


def test(testObj: unittest.TestCase, intervals: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.minMeetingRooms(intervals)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[0, 30], [5, 10], [15, 20]], 2)

    def test_2(self):
        test(self, [[7, 10], [2, 4]], 1)


if __name__ == "__main__":
    unittest.main()

"""

"""

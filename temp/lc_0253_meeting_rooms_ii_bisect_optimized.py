import unittest
from bisect import insort_left
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        going_on: List[int] = []
        for start, end in intervals:
            if going_on and going_on[-1] <= start:
                going_on.pop()

            insort_left(going_on, x=end, key=lambda x: -x)

        return len(going_on)


def test(testObj: unittest.TestCase, intervals: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.minMeetingRooms(intervals)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 30], [5, 10], [15, 20]], 2)

    def test_2(self):
        test(self,   [[7, 10], [2, 4]], 1)

    def test_3(self):
        test(self,   [[1, 3], [3, 5], [5, 7], [2, 4], [4, 6], [6, 8]], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
165 ms
Beats
57.17%
'''

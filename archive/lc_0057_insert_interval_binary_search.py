import unittest
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        # firstly, find the first/left overlap
        # x=2, 1 [2] 3, F [T] T
        left = bisect_left(intervals, x=newInterval[0], key=lambda x: x[1])
        if left == n:
            intervals.append(newInterval)
            return intervals
        # secondly, find the last/right overlap
        # x=2, 1 2 [3], F [F] T
        right = bisect_right(intervals, x=newInterval[1], key=lambda x: x[0])
        if right == 0:
            intervals.insert(0, newInterval)
            return intervals
        right -= 1

        # if left > right, there is no overlap
        if left <= right:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right][1])
        return intervals[:left] + [newInterval] + intervals[right + 1 :]


def test(
    testObj: unittest.TestCase,
    intervals: List[List[int]],
    newInterval: List[int],
    expected: List[List[int]],
) -> None:
    so = Solution()
    actual = so.insert(intervals, newInterval)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    # overlap with one / left
    def test_1(self):
        test(self, [[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])

    # overlap with two
    def test_2(self):
        test(
            self,
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        )

    # in the middle, no overlap
    def test_3(self):
        test(self, [[1, 3], [6, 9]], [4, 5], [[1, 3], [4, 5], [6, 9]])

    # overlap with one / right
    def test_4(self):
        test(self, [[1, 3], [6, 9]], [5, 7], [[1, 3], [5, 9]])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
79 ms
Beats
97.92%
"""

import unittest
from bisect import bisect_left, bisect_right


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
        newStart, newEnd = newInterval
        left = bisect_left(intervals, x=newStart, key=lambda interval: interval[1])
        if left < n and intervals[left][0] <= newEnd:
            newStart = min(intervals[left][0], newStart)
            newEnd = max(intervals[left][1], newEnd)

        right = bisect_right(intervals, x=newEnd, key=lambda interval: interval[0]) - 1
        if right > 0 and intervals[right][1] >= newStart:
            newStart = min(intervals[right][0], newStart)
            newEnd = max(intervals[right][1], newEnd)

        return intervals[:left] + [[newStart, newEnd]] + intervals[right + 1:]


def test(
    testObj: unittest.TestCase,
    intervals: list[list[int]],
    newInterval: list[int],
    expected: list[list[int]],
) -> None:
    so = Solution()
    actual = so.insert(intervals, newInterval)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])

    def test_2(self):
        test(
            self,
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        )

    def test_3(self):
        test(self, [], [5, 7], [[5, 7]])

    def test_4(self):
        test(self, [[1, 5]], [0, 1], [[0, 5]])


if __name__ == "__main__":
    unittest.main()


"""
Runtime
80 ms
Beats
91.29%
"""

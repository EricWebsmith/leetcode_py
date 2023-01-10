import unittest
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        if toBeRemoved[0] >= intervals[-1][1]:
            return []
        if toBeRemoved[1] <= intervals[0][0]:
            return []

        # left and right is indices we want to delete
        # we delete intervals [left, right)
        # left is included, right is not
        # if left + 1 == right, there is only one to delete
        left = bisect_left(intervals, x=toBeRemoved[0], key=lambda x: x[0])
        right = bisect_right(intervals, x=toBeRemoved[1], key=lambda x: x[1])

        # so if left == right, we delete one of them
        # if left > right+1, the toBeRemoved does not overlap intervals
        # there is nothing to delete
        if left > right+1:
            return intervals

        # if left == right+1,
        # toBeRemoved is inside intervals[left-1]
        # we need to split it into two
        # in python we can simply use intervals[i-1:i] = [[a,b],[c,b]]
        if left == right+1:
            intervals[left-1:left] = [
                [intervals[left-1][0], toBeRemoved[0]], [toBeRemoved[1], intervals[left-1][1]]]
            return intervals

        # if left == right, there is nothing to delete
        # and the following has no effect
        # but we still have to deal with intervals[left]
        intervals = intervals[:left] + intervals[right:]
        if left > 0:
            intervals[left-1][1] = min(intervals[left-1][1], toBeRemoved[0])
        if left < len(intervals):
            intervals[left][0] = max(intervals[left][0], toBeRemoved[1])

        return intervals


def test(testObj: unittest.TestCase, intervals: List[List[int]],
         toBeRemoved: List[int], expected: List[List[int]]) -> None:

    so = Solution()
    actual = so.removeInterval(intervals, toBeRemoved)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 2], [3, 4], [5, 7]],  [1, 6], [[0, 1], [6, 7]])

    def test_2(self):
        test(self,   [[0, 5]],  [2, 3], [[0, 2], [3, 5]])

    def test_3(self):
        test(self,   [[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]],
             [-1, 4], [[-5, -4], [-3, -2], [4, 5], [8, 9]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 394 ms, faster than 92.56%
Memory Usage: 20.8 MB, less than 73.55%
'''

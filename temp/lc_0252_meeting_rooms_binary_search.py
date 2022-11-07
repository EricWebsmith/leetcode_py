import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        arr: List[List[int]] = []
        for start, end in intervals:
            index = bisect_left(arr, start, key=lambda x: x[0])
            if index-1 >= 0 and arr[index-1][1] > start:
                return False
            if index < len(arr) and arr[index][0] < end:
                return False

            arr.insert(index, [start, end])

        return True


def test(testObj: unittest.TestCase, intervals: List[List[int]], expected: bool) -> None:

    so = Solution()
    actual = so.canAttendMeetings(intervals)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 30], [5, 10], [15, 20]], False)

    def test_2(self):
        test(self,   [[7, 10], [2, 4]], True)

    def test_3(self):
        test(self,   [[1, 3], [3, 5], [5, 7], [2, 4]], False)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
171 ms
Beats
41.66%
'''

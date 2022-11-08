import unittest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif interval[0] > newInterval[1]:
                return ans + [newInterval] + intervals[i:]
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        return ans + [newInterval]


def test(testObj: unittest.TestCase, intervals: List[List[int]], newInterval: List[int], expected: List[List[int]]) -> None:

    so = Solution()
    actual = so.insert(intervals, newInterval)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    # overlap with one / left
    def test_1(self):
        test(self,   [[1, 3], [6, 9]],  [2, 5], [[1, 5], [6, 9]])

    # overlap with two
    def test_2(self):
        test(self,   [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
             [4, 8], [[1, 2], [3, 10], [12, 16]])

    # in the middle, no overlap
    def test_3(self):
        test(self,   [[1, 3], [6, 9]],  [4, 5], [[1, 3], [4, 5], [6, 9]])

    # overlap with one / right
    def test_4(self):
        test(self,   [[1, 3], [6, 9]],  [5, 7], [[1, 3], [5, 9]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
86 ms
Beats
92.18%
'''

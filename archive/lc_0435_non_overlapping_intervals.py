import unittest
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        ans = 0
        for s, e in intervals[1:]:
            if s >= prev_end:
                prev_end = e
            else:
                prev_end = min(prev_end, e)
                ans += 1

        return ans


def test(testObj: unittest.TestCase, intervals: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.eraseOverlapIntervals(intervals)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 2], [2, 3], [3, 4], [1, 3]], 1)

    def test_2(self):
        test(self, [[1, 2], [1, 2], [1, 2]], 2)

    def test_3(self):
        test(self, [[1, 2], [2, 3]], 0)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
2244 ms
Beats
73.71%
"""

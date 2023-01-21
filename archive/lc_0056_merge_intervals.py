import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans: List[List[int]] = [intervals[0]]

        for start, end in intervals[1:]:
            if ans[-1][1] >= start:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])

        return ans


def test(
    testObj: unittest.TestCase, intervals: List[List[int]], expected: List[List[int]]
) -> None:

    so = Solution()
    actual = so.merge(intervals)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])

    def test_2(self):
        test(self, [[1, 4], [4, 5]], [[1, 5]])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
346 ms
Beats
42.38%
"""

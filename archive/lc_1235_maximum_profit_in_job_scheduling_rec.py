import unittest
from bisect import bisect_left
from functools import cache
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        @cache
        def dfs(i):
            if i == n:
                return 0

            j = bisect_left(jobs, x=jobs[i][1], key=lambda x: x[0])

            one = jobs[i][2] + dfs(j)
            two = dfs(i+1)
            return max(one, two)

        return dfs(0)


def test(testObj: unittest.TestCase, startTime: List[int], endTime: List[int],
         profit: List[int], expected: int) -> None:
    so = Solution()
    actual = so.jobScheduling(startTime, endTime, profit)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 3],  [3, 4, 5, 6],  [50, 10, 40, 70], 120)

    def test_2(self):
        test(self,   [1, 2, 3, 4, 6],  [3, 5, 10, 6, 9],
             [20, 20, 100, 70, 60], 150)

    def test_3(self):
        test(self,   [1, 1, 1],  [2, 3, 4],  [5, 6, 4], 6)


if __name__ == '__main__':
    unittest.main()

'''

'''

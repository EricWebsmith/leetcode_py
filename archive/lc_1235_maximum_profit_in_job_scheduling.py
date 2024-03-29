import unittest
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        events = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        events.sort()
        post_max = [0] * n
        moving_max = events[-1][2]
        for i in range(n - 1, -1, -1):
            moving_max = max(moving_max, events[i][2])
            post_max[i] = moving_max

        cache: dict = dict()

        def dfs(index):
            if index in cache:
                return cache[index]
            if index == n - 1:
                return events[-1][2]
            # take this job

            _, end, value = events[index]
            take_this = value
            # binary
            left = index + 1
            right = n
            while left < right:
                mid = (left + right) >> 1
                if events[mid][0] < end:
                    left = mid + 1
                else:
                    right = mid

            next_index = left
            if next_index < n:
                take_this = value + dfs(next_index)
            # not take this job
            not_take_this = dfs(index + 1)
            ans = max(take_this, not_take_this)
            cache[index] = ans
            return ans

        return dfs(0)


def test(
    testObj: unittest.TestCase,
    startTime: List[int],
    endTime: List[int],
    profit: List[int],
    expected: int,
) -> None:

    so = Solution()
    actual = so.jobScheduling(startTime, endTime, profit)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120)

    def test_2(self):
        test(self, [1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150)

    def test_3(self):
        test(self, [1, 1, 1], [2, 3, 4], [5, 6, 4], 6)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 762 ms, faster than 70.45%
Memory Usage: 45 MB, less than 26.29%
"""

import itertools
import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_need_days(mid):
            index = 0
            pre_sum = 0
            need_days = 0
            while index < n:
                index = bisect_right(pre_sums, pre_sum + mid)
                pre_sum = pre_sums[index - 1]
                need_days += 1
            return need_days

        n = len(weights)
        pre_sums = list(itertools.accumulate(weights))
        print(pre_sums)
        left = max(weights)
        right = pre_sums[-1]
        while left < right:
            mid = (left + right) >> 1
            need_days = get_need_days(mid)
            if need_days > days:
                left = mid + 1
            else:
                right = mid

        return left


def test(
    testObj: unittest.TestCase, weights: List[int], days: int, expected: int
) -> None:

    so = Solution()
    actual = so.shipWithinDays(weights, days)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15)

    def test_2(self):
        test(self, [3, 2, 2, 4, 1, 4], 3, 6)

    def test_3(self):
        test(self, [1, 2, 3, 1, 1], 4, 3)

    def test_4(self):
        test(self, [1], 1, 1)

    def test_5(self):
        test(self, [1, 2, 3, 4, 5], 2, 9)

    def test_6(self):
        test(self, [1, 2, 3, 4, 5], 3, 6)

    def test_7(self):
        test(self, [1, 2, 3, 4, 5], 4, 5)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 639 ms, faster than 72.24%
Memory Usage: 18.4 MB, less than 7.42%
"""

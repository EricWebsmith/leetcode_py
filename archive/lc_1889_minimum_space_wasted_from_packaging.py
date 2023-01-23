import sys
import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(packages)
        packages.sort()
        pre_sum = [0]

        for i in range(n):
            pre_sum.append((pre_sum[-1] + packages[i]))

        best_waste = sys.maxsize

        for box_arr in boxes:
            box_arr.sort()
            if box_arr[-1] < packages[-1]:
                continue

            waste = 0
            pre_index = 0
            for box_size in box_arr:
                index = bisect_right(packages, box_size)
                waste += box_size * (index - pre_index) - (pre_sum[index] - pre_sum[pre_index])
                pre_index = index

            best_waste = min(best_waste, waste)

        return -1 if best_waste == sys.maxsize else best_waste % MOD


def test(
    testObj: unittest.TestCase,
    packages: List[int],
    boxes: List[List[int]],
    expected: int,
) -> None:

    so = Solution()

    actual = so.minWastedSpace(packages, boxes)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [2, 3, 5], [[4, 8], [2, 8]], 6)

    def test_2(self):
        test(self, [2, 3, 5], [[1, 4], [2, 3], [3, 4]], -1)

    def test_3(self):
        test(self, [3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]], 9)

    def test_4(self):
        test(
            self,
            [3, 5, 8, 10, 11, 12],
            [[12], [11, 9], [10, 5, 14], [3, 5, 8, 10, 11, 12]],
            0,
        )

    def test_5(self):
        test(
            self,
            [3, 5, 8, 10, 11, 12],
            [[12], [11, 9], [10, 5, 14], [2, 4, 6, 8, 10, 12, 14]],
            3,
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 1679 ms, faster than 86.67%
Memory Usage: 38.8 MB, less than 29.17%
"""

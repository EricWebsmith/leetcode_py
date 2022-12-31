import unittest
from bisect import bisect_left, insort_left
from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = - 2 ** 31

    def update_result(self, nums: List[int], k: int) -> None:
        sum = 0
        sorted_sum = [0]
        for num in nums:
            sum += num
            x_index = bisect_left(sorted_sum,  sum - k)
            if x_index < len(sorted_sum):
                self.result = max(sum - sorted_sum[x_index], self.result)

            insort_left(sorted_sum, sum)

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for r_start in range(m):
            row_sum = [0] * n

            for r in range(r_start, m):
                for c in range(n):
                    row_sum[c] += matrix[r][c]

                self.update_result(row_sum, k)

                if self.result == k:
                    return self.result

        return self.result


def test(testObj: unittest.TestCase, matrix: List[List[int]], k: int, expected: int) -> None:

    so = Solution()
    actual = so.maxSumSubmatrix(matrix, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 0, 1], [0, -2, 3]],  2, 2)

    def test_2(self):
        test(self,   [[2, 2, -1]],  3, 3)

    def test_3(self):
        test(self,   [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 10, 10)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1528 ms, faster than 98.02%
Memory Usage: 14.8 MB, less than 57.31%
'''

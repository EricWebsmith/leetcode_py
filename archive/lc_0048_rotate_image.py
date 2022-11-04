import unittest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n // 2 + (n % 2)):
            for c in range(n//2):
                t = matrix[r][c]
                matrix[r][c] = matrix[n-1-c][r]
                matrix[n-1-c][r] = matrix[n-1-r][n-1-c]
                matrix[n-1-r][n-1-c] = matrix[c][n-1-r]
                matrix[c][n-1-r] = t


def test(testObj: unittest.TestCase, matrix: List[List[int]], expected: None) -> None:
    so = Solution()
    so.rotate(matrix)
    testObj.assertEqual(matrix, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_2(self):
        test(self,   [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], [
             [15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
72 ms
Beats
36.19%
'''

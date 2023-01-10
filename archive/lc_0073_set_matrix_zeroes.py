import unittest
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        rows: list = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows.append(r)
                    break

        cols: list = []
        for c in range(n):
            for r in range(m):
                if matrix[r][c] == 0:
                    cols.append(c)
                    break

        for r in rows:
            for c in range(n):
                matrix[r][c] = 0

        for c in cols:
            for r in range(m):
                matrix[r][c] = 0


def test(testObj: unittest.TestCase, matrix: List[List[int]], expected: int) -> None:

    so = Solution()
    so.setZeroes(matrix)
    testObj.assertEqual(matrix, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
             [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_2(self):
        test(self,   [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
             [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 165 ms, faster than 74.40%
Memory Usage: 14.9 MB, less than 16.28%
'''

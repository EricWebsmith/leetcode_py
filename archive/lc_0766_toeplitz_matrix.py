import unittest
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            c = 0
            first = matrix[r][c]
            i = 1
            while r + i < m and c + i < n:
                if matrix[r + i][c + i] != first:
                    return False
                i += 1

        for c in range(n):
            r = 0
            first = matrix[r][c]
            i = 1
            while r + i < m and c + i < n:
                if matrix[r + i][c + i] != first:
                    return False
                i += 1

        return True


def test(testObj: unittest.TestCase, matrix: List[List[int]], expected: bool) -> None:

    so = Solution()

    actual = so.isToeplitzMatrix(matrix)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True)

    def test_2(self):
        test(self, [[1, 2], [2, 2]], False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
88 ms
Beats
95.34%
"""

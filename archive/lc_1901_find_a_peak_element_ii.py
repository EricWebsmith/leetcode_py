import unittest
from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        for r in range(m):
            row_max = 0
            row_max_index = 0
            for c in range(n):
                if mat[r][c] > row_max:
                    row_max = mat[r][c]
                    row_max_index = c
            if r == m - 1:
                return [r, row_max_index]
            if mat[r][row_max_index] > mat[r + 1][row_max_index]:
                return [r, row_max_index]

        return [-1, -1]


def test(testObj: unittest.TestCase, mat: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.findPeakGrid(mat)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 4], [3, 2]], [0, 1])

    def test_2(self):
        test(self, [[10, 20, 15], [21, 30, 14], [7, 16, 32]], [1, 1])


if __name__ == "__main__":
    unittest.main()

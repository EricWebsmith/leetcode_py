import unittest
from typing import List


class BinaryMatrix(object):
    def __init__(self, mat: List[List[int]]) -> None:
        self.mat = mat
        self.m = len(mat)
        self.n = len(mat[0])

    def get(self, row: int, col: int) -> int:
        return self.mat[row][col]

    def dimensions(self) -> List[int]:
        return [self.m, self.n]


class Solution:
    def __init__(self) -> None:
        self.binaryMatrix : BinaryMatrix

    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        self.binaryMatrix = binaryMatrix
        m, n = binaryMatrix.dimensions()

        def find_1(row, right=n):
            left = 0
            while left < right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(row, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            return right

        right = find_1(0)
        for r in range(1, m):
            if right < n and binaryMatrix.get(r, right) == 0:
                continue
            right = find_1(r, right)

        return right if right < n else -1


def test(testObj: unittest.TestCase, mat: List[List[int]], expected: int) -> None:

    binaryMatrix = BinaryMatrix(mat)
    so = Solution()
    actual = so.leftMostColumnWithOne(binaryMatrix)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[0, 0], [1, 1]], 0)

    def test_2(self):
        test(self, [[0, 0], [0, 1]], 1)

    def test_3(self):
        test(self, [[0, 0], [0, 0]], -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 137 ms, faster than 70.46%
Memory Usage: 14.2 MB, less than 50.45%
"""

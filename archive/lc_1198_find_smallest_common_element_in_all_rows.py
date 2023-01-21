import unittest
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cur_max = mat[0][0]
        cnt = 0
        p = [0] * m
        while True:

            for r in range(m):
                while p[r] < n and mat[r][p[r]] < cur_max:
                    p[r] += 1

                if p[r] == n:
                    return -1

                if cur_max == mat[r][p[r]]:
                    cnt += 1
                else:
                    cur_max = mat[r][p[r]]
                    cnt = 1

                if cnt == m:
                    return cur_max

        return -1


def test(testObj: unittest.TestCase, mat: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.smallestCommonElement(mat)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]],
            5,
        )

    def test_2(self):
        test(self, [[1, 2, 3], [2, 3, 4], [2, 3, 5]], 2)

    def test_3(self):
        test(self, [[1, 2, 3], [2, 3, 4], [2, 3, 5], [3, 4, 5]], 3)

    def test_4(self):
        test(self, [[1, 2, 3], [2, 3, 4], [2, 3, 5], [3, 4, 5], [4, 5, 6]], -1)

    def test_5(self):
        test(self, [[1, 2, 3], [4, 5, 6]], -1)

    def test_6(self):
        test(self, [[1, 2, 3]], 1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
493 ms
Beats
97.9%
"""

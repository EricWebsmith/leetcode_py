import unittest
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        non_obstacles = 0
        r0, c0 = 0, 0
        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    r0 = r
                    c0 = c

        paths = 0

        def backtrack(r, c, remain):
            nonlocal paths

            if grid[r][c] == 2 and remain == 1:
                paths += 1
                return

            t = grid[r][c]
            grid[r][c] = -4
            remain -= 1

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] < 0:
                    continue

                backtrack(nr, nc, remain)

            grid[r][c] = t

        backtrack(r0, c0, non_obstacles)

        return paths


def test(testObj: unittest.TestCase, grid: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.uniquePathsIII(grid)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2)

    def test_2(self):
        test(self,   [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4)

    def test_3(self):
        test(self,   [[0, 1], [2, 0]], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
69 ms
Beats
81.47%
'''

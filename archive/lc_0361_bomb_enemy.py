
import unittest
from typing import List

import numpy as np


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vertical_kills = np.zeros([m, n], dtype=int)
        horizontal_kills = np.zeros([m, n], dtype=int)

        for r in range(m):
            previous_block = -1
            kill = 0
            for c in range(n):
                if grid[r][c] == 'W':
                    horizontal_kills[r][previous_block+1:c+1] = kill
                    previous_block = c
                    kill = 0
                elif grid[r][c] == 'E':
                    kill += 1

                if c == n-1:
                    horizontal_kills[r][previous_block+1:c+1] = kill

        for c in range(n):
            previous_block = -1
            kill = 0
            for r in range(m):
                if grid[r][c] == 'W':
                    vertical_kills[previous_block+1:r+1, c] = kill
                    previous_block = r
                    kill = 0
                elif grid[r][c] == 'E':
                    kill += 1

                if r == m - 1:
                    vertical_kills[previous_block+1:r+1, c] = kill

        max_kill = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '0':
                    max_kill = max(max_kill, vertical_kills[r][c] + horizontal_kills[r][c])

        return max_kill


def test(testObj: unittest.TestCase, grid: List[List[str]], expected: int) -> None:

    so = Solution()
    actual = so.maxKilledEnemies(grid)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,   [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]], 3)

    def test_2(self):
        test(self,   [["W", "W", "W"], ["0", "0", "0"], ["E", "E", "E"]], 1)

    def test_3(self):
        test(self,   [["W", "E", "E", "E", "E", "0"], ["E", "E", "E", "E", "E", "W"]], 4)


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 1161 ms, faster than 58.55%
Memory Usage: 41.4 MB, less than 12.58%
"""

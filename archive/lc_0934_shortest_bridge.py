import unittest
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
        island1 = deque[tuple[int, int]]()

        def dfs(r, c):
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    island1.append([nr, nc])
                    dfs(nr, nc)

        def findIsland1():
            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        return dfs(r, c)

        findIsland1()

        bridge = 0
        while island1:
            for _ in range(len(island1)):
                r, c = island1.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 2:
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            island1.append((nr, nc))
                        elif grid[nr][nc] == 1:
                            return bridge
            bridge += 1
        return bridge


def test(testObj: unittest.TestCase, grid: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.shortestBridge(grid)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[0, 1], [1, 0]], 1)

    def test_2(self):
        test(self, [[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2)

    def test_3(self):
        test(
            self,
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ],
            1,
        )

    def test_4(self):
        test(
            self,
            [
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 1],
                [0, 0, 1, 1, 0],
            ],
            1,
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime
536 ms
Beats
79.41%
"""

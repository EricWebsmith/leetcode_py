import unittest
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque([(0, 0, k, 0)])
        seen = set()
        while q:
            r, c, left, steps = q.popleft()
            if (r, c, left) in seen or left < 0:
                continue

            if (r, c) == (m - 1, n - 1):
                return steps

            seen.add((r, c, left))
            if grid[r][c] == 1:
                left -= 1
            for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    q.append((nr, nc, left, steps + 1))

        return -1


def test(
    testObj: unittest.TestCase, grid: List[List[int]], k: int, expected: int
) -> None:
    so = Solution()
    actual = so.shortestPath(grid, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6)

    def test_2(self):
        test(self, [[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
815 ms
Beats
42.73%
"""

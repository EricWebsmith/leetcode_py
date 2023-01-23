import unittest
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # the number of the existing buildings
        n_buildings = sum(cell for row in grid for cell in row if cell == 1)

        # distSum = access = [[0 for c in range(C)] for r in range(R)]
        # # record the cnt of accessible building to this cell # this cannot work
        # record the cnt of accessible building to this cell
        access_grid = [[0 for c in range(n)] for r in range(m)]
        # record the accumulated distances from other buildings to this cell
        dist_grid = [[0 for c in range(n)] for r in range(m)]

        # this is just for one building to reach to other cells
        def bfs(nr, nc):
            visited = [[False for c in range(n)] for r in range(m)]  # just for this node

            visited[nr][nc] = True
            # accessible buildings from this building (include itself)
            buildings_count = 1
            # start point and the distance from start point to this point
            q = deque([(nr, nc, 0)])
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while q:
                r, c, d = q.popleft()  # dist: from the start point to this point
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if grid[nr][nc] == 0:
                            q.append((nr, nc, d + 1))
                            # this building has been accessed by one traversal
                            access_grid[nr][nc] += 1
                            # from the start point (building) to this cell
                            dist_grid[nr][nc] += d + 1
                        elif grid[nr][nc] == 1:
                            buildings_count += 1

            # if it is not equal, some of the buildings cannot be accessed at this point
            return buildings_count == n_buildings

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    if not bfs(x, y):  # if any build cannot reach the other build, return false
                        return -1

        return min(
            [
                dist_grid[i][j]
                for i in range(m)
                for j in range(n)
                if grid[i][j] == 0 and access_grid[i][j] == n_buildings
            ]
            or [-1]
        )


def test(testObj: unittest.TestCase, grid: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.shortestDistance(grid)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 7)

    def test_2(self):
        test(self, [[1, 0]], 1)

    def test_3(self):
        test(self, [[1]], -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 2009 ms, faster than 99.92%
Memory Usage: 14.2 MB, less than 94.69%
"""

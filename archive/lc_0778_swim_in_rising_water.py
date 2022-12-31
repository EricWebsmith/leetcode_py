import unittest
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> int:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1

        if px > py:
            self.p[px] = py
        else:
            self.p[py] = px
        self.e += 1
        return 0


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        nn = n * n
        depth_position_dict = [0] * (nn)
        for r in range(n):
            for c in range(n):
                depth_position_dict[grid[r][c]] = [r, c]

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def validate(r, c):
            if r < 0 or r == n:
                return False
            if c < 0 or c == n:
                return False
            return True

        dsu = DSU(nn)
        top_left = grid[0][0]
        bottom_right = grid[n-1][n-1]
        for depth, (r, c) in enumerate(depth_position_dict):
            for dr, dc in dirs:
                neighbor_r = r+dr
                neighbor_c = c+dc
                if not validate(neighbor_r, neighbor_c):
                    continue

                neighbor_depth = grid[neighbor_r][neighbor_c]
                if neighbor_depth > depth:
                    continue

                dsu.union(depth, neighbor_depth)
            if dsu.find(top_left) == dsu.find(bottom_right):
                return depth

        return 0


def test(testObj: unittest.TestCase, grid: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.swimInWater(grid)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 2], [1, 3]], 3)

    def test_2(self):
        test(self,   [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
             12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], 16)

    def test_3(self):
        test(self,   [[0]], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 122 ms, faster than 88.35%
Memory Usage: 14.5 MB, less than 90.64%
'''

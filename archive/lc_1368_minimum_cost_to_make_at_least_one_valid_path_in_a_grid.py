import unittest
from typing import List
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        right = 1
        left = 2
        down = 3
        up = 4
        max_distance = 1_000_000

        m = len(grid)
        n = len(grid[0])
        dp = [[max_distance] * n for r in range(m)]
        dp[0][0] = 0
        q = deque()
        q.append((0, 0))

        while q:
            r, c = q.popleft()
            for dr, dc, dir in [[0, 1, right], [1, 0, down], [0, -1, left], [-1, 0, up]]:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr == m:
                    continue
                if nc < 0 or nc == n:
                    continue
                to = int(grid[r][c] == dir)
                if dp[nr][nc] <= dp[r][c]+1-to:
                    continue
                dp[nr][nc] = dp[r][c]+1-to
                q.append((nr, nc))

        return dp[m-1][n-1]


def test(testObj: unittest.TestCase, grid: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.minCost(grid)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 1, 1, 1], [2, 2, 2, 2],
             [1, 1, 1, 1], [2, 2, 2, 2]], 3)

    def test_2(self):
        test(self,   [[1, 1, 3], [3, 2, 2], [1, 1, 4]], 0)

    def test_3(self):
        test(self,   [[1, 2], [4, 3]], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 3758 ms, faster than 5.22% of Python3 online submissions for Minimum Cost to Make at Least One Valid Path in a Grid.
Memory Usage: 14.5 MB, less than 98.26% of Python3 online submissions for Minimum Cost to Make at Least One Valid Path in a Grid.
'''

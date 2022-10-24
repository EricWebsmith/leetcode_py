import unittest
from typing import List
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m = len(rooms)
        n = len(rooms[0])

        def bfs(r, c):
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            q = deque()
            q.append((r, c))
            while q:
                cr, cc = q.popleft()
                cv = rooms[cr][cc]
                for dr, dc in dirs:
                    nr = cr + dr
                    nc = cc + dc
                    if nr < 0 or nr == m:
                        continue
                    if nc < 0 or nc == n:
                        continue
                    if rooms[nr][nc] == -1:
                        continue
                    if rooms[nr][nc] <= cv+1:
                        continue

                    rooms[nr][nc] = cv+1
                    q.append((nr, nc))

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    bfs(r, c)


def test(testObj: unittest.TestCase, rooms: List[List[int]], expected: None) -> None:

    so = Solution()

    so.wallsAndGates(rooms)

    testObj.assertEqual(rooms, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1,
             2147483647, -1], [0, -1, 2147483647, 2147483647]], [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]])

    def test_2(self):
        test(self,   [[-1]], [[-1]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 292 ms, faster than 88.00% of Python3 online submissions for Walls and Gates.
Memory Usage: 16.5 MB, less than 97.61% of Python3 online submissions for Walls and Gates.
'''

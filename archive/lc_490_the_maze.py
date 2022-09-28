import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        stack = []
        stack.append(start)
        while stack:
            r, c = stack.pop()
            visited.add((r, c))
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr = r
                nc = c
                while 0 <= nr+dr < m and 0 <= nc+dc < n and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc

                if nr == destination[0] and nc == destination[1]:
                    return True

                if (nr, nc) in visited:
                    continue

                stack.append([nr, nc])

        return False


def test(testObj: unittest.TestCase, maze: List[List[int]], start: List[int], destination: List[int], expected: bool) -> None:

    so = Solution()

    actual = so.hasPath(maze, start, destination)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [
             1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],  [0, 4],  [4, 4], True)

    def test_2(self):
        test(self,   [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [
             1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],  [0, 4],  [3, 2], False)

    def test_3(self):
        test(self,   [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [
             0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],  [4, 3],  [0, 1], False)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 295 ms, faster than 92.32% of Python3 online submissions for The Maze.
Memory Usage: 14.8 MB, less than 45.07% of Python3 online submissions for The Maze.
'''

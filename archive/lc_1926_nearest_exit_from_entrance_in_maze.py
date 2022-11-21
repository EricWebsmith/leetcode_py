import unittest
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        q = deque([[entrance[0], entrance[1], 0]])
        while q:
            r, c, d = q.popleft()
            # visit four neighours
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr = r+dr
                nc = c+dc
                # contine if the position is invalid.
                if nr < 0 or nr == m or nc < 0 or nc == n:
                    continue

                # continue if wall / visited
                if maze[nr][nc] == '+':
                    continue

                # if the cell is at the border, it is an exit.
                if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:
                    return d+1

                # make the visited cell a wall, so we will not visit it again.
                maze[nr][nc] = '+'
                q.append([nr, nc, d+1])

        return -1


def test(testObj: unittest.TestCase, maze: List[List[str]], entrance: List[int], expected: int) -> None:
    so = Solution()
    actual = so.nearestExit(maze, entrance)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [["+", "+", ".", "+"], [".", ".", ".", "+"],
             ["+", "+", "+", "."]],  [1, 2], 1)

    def test_2(self):
        test(self,   [["+", "+", "+"], [".", ".", "."],
             ["+", "+", "+"]],  [1, 0], 2)

    def test_3(self):
        test(self,   [[".", "+"]],  [0, 0], -1)

    def test_4(self):
        test(self,   [["+", "+", "+", "+"], [".", ".", ".", "."],
             ["+", "+", "+", "+"]],  [1, 0], 3)

    def test_5(self):
        test(self,   [["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+", ".",
             "+", ".", "+"], ["+", ".", ".", ".", "+", ".", "+"], ["+", "+", "+", "+", "+", ".", "+"]],  [3, 2], 4)

    def test_6(self):
        test(self,   [["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+", ".",
             "+", ".", "+"], ["+", ".", ".", ".", "+", ".", "+"], ["+", "+", "+", "+", "+", "+", "."]],  [0, 1], -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
767 ms
Beats
96.21%
'''

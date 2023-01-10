import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def __init__(self) -> None:
        self.found = False

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        MAX_PATH = 1000000
        m = len(maze)
        n = len(maze[0])

        shortest_mat = [[MAX_PATH] * n for i in range(m)]

        q = [(0, start[0], start[1])]

        while len(q) > 0:
            p, r, c = heappop(q)

            if shortest_mat[r][c] <= p:
                continue
            shortest_mat[r][c] = p

            if r == destination[0] and c == destination[1]:
                return p

            # top down left right
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r_next = r
                c_next = c
                p_next = p
                while r_next + dr >= 0 and r_next + dr < m  \
                        and c_next + dc >= 0 and c_next + dc < n  \
                        and maze[r_next + dr][c_next + dc] == 0:
                    r_next += dr
                    c_next += dc
                    p_next += 1

                heappush(q, ((p_next, r_next, c_next)))  # type: ignore

        return -1 if shortest_mat[destination[0]][destination[1]] == MAX_PATH \
            else shortest_mat[destination[0]][destination[1]]


def test(testObj: unittest.TestCase, maze: List[List[int]], start: List[int],
         destination: List[int], expected: int) -> None:

    so = Solution()
    actual = so.shortestDistance(maze, start, destination)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],  [0, 4],  [4, 4], 12)

    def test_2(self):
        test(self,   [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],  [0, 4],  [3, 2], -1)

    def test_3(self):
        test(self,   [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],  [4, 3],  [0, 1], -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 315 ms, faster than 93.93%
Memory Usage: 14.4 MB, less than 78.57%
'''

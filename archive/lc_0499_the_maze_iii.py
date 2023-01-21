import unittest
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findShortestWay(
        self, maze: List[List[int]], ball: List[int], hole: List[int]
    ) -> str:
        m, n = len(maze), len(maze[0])
        q = [(0, ball[0], ball[1], "")]
        heapify(q)
        stopped = {(ball[0], ball[1]): 0}
        dirs = [(0, -1, "l"), (0, 1, "r"), (-1, 0, "u"), (1, 0, "d")]

        ans_with_dist = []
        while q:
            dist, r, c, path = heappop(q)

            for dr, dc, dir in dirs:
                nr = r
                nc = c
                d = 0
                # keep moving
                while (
                    0 <= nr + dr < m
                    and 0 <= nc + dc < n
                    and maze[nr + dr][nc + dc] != 1
                ):
                    nr += dr
                    nc += dc
                    d += 1
                    if nr == hole[0] and nc == hole[1]:
                        ans_with_dist.append((-dist - d, path + dir))
                        break

                # stop moving
                if d > 0 and dist + d <= stopped.get((nr, nc), m * n):
                    stopped[(nr, nc)] = dist + d
                    heappush(q, (dist + d, nr, nc, path + dir))  # type: ignore

        if len(ans_with_dist) == 0:
            return "impossible"

        ans_with_dist.sort()

        min_dist = -ans_with_dist[-1][0]
        ans: list = []
        while ans_with_dist and ans_with_dist[-1][0] == -min_dist:
            ans.append(ans_with_dist[-1][1])
            ans_with_dist.pop()

        ans.sort()

        return ans[0]


def test(
    testObj: unittest.TestCase,
    maze: List[List[int]],
    ball: List[int],
    hole: List[int],
    expected: str,
) -> None:
    so = Solution()
    actual = so.findShortestWay(maze, ball, hole)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 1, 0, 0, 0],
            ],
            [4, 3],
            [0, 1],
            "lul",
        )

    def test_2(self):
        test(
            self,
            [
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 1, 0, 0, 0],
            ],
            [4, 3],
            [3, 0],
            "impossible",
        )

    def test_3(self):
        test(
            self,
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1],
            ],
            [0, 4],
            [3, 5],
            "dldr",
        )

    def test_4(self):
        test(
            self,
            [
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 1, 0, 0, 0],
            ],
            [4, 3],
            [0, 1],
            "ul",
        )

    def test_5(self):
        test(
            self,
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
            ],
            [4, 3],
            [0, 1],
            "ul",
        )

    def test_6(self):
        test(self, [[0, 0]], [0, 0], [0, 1], "r")

    def test_7(self):
        test(self, [[0, 0]], [0, 1], [0, 0], "l")

    def test_8(self):
        test(
            self,
            [
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            ],
            [2, 4],
            [7, 6],
            "drdrdrdldl",
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 71 ms, faster than 83.66%
Memory Usage: 13.9 MB, less than 99.26%
"""

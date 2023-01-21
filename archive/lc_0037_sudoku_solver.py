import unittest
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.solved = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        def could_place(d, r, c):
            return not (d in rows[r] or d in columns[c] or d in boxes[box_index(r, c)])

        def place_number(d, r, c):
            rows[r][d] += 1
            columns[c][d] += 1
            boxes[box_index(r, c)][d] += 1
            board[r][c] = str(d)

        def remove_number(d, r, c):
            del rows[r][d]
            del columns[c][d]
            del boxes[box_index(r, c)][d]
            board[r][c] = "."

        def place_next_numbers(r, c):
            if c == N - 1 and r == N - 1:
                self.solved = True
            else:
                if c == N - 1:
                    backtrack(r + 1, 0)
                else:
                    backtrack(r, c + 1)

        def backtrack(r=0, c=0):
            if board[r][c] == ".":
                for d in range(1, 10):
                    if could_place(d, r, c):
                        place_number(d, r, c)
                        place_next_numbers(r, c)
                        if not self.solved:
                            remove_number(d, r, c)
            else:
                place_next_numbers(r, c)

        n = 3
        N = n * n

        def box_index(r, c):
            return (r // n) * n + c // n

        rows: list[dict] = [defaultdict(int) for i in range(N)]
        columns: list[dict] = [defaultdict(int) for i in range(N)]
        boxes: list[dict] = [defaultdict(int) for i in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] != ".":
                    d = int(board[r][c])
                    place_number(d, r, c)

        self.solved = False
        backtrack()


def test(testObj: unittest.TestCase, board: List[List[str]], expected: int) -> None:

    so = Solution()
    so.solveSudoku(board)
    testObj.assertEqual(board, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 182 ms, faster than 79.22%
Memory Usage: 14.1 MB, less than 20.66%
"""

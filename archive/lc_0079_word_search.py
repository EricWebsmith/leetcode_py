import unittest
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows, n_cols = len(board), len(board[0])

        visiting = set()

        def dfs(row, col, i):
            if row == -1 or row == n_rows or col == -1 or col == n_cols:
                return False

            if board[row][col] != word[i]:
                return False

            if (row, col) in visiting:
                return False

            if i == len(word) - 1:
                return True

            visiting.add((row, col))
            # we return true betwen visiting.add and visiting .remove
            # because true is the end,
            # no need to clean up

            # dr, dc = delta row, delta col
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if dfs(row + dr, col + dc, i + 1):
                    return True

            visiting.remove((row, col))
            return False

        for row in range(n_rows):
            for col in range(n_cols):
                if dfs(row, col, 0):
                    return True

        return False


def test(
    testObj: unittest.TestCase, board: List[List[str]], word: str, expected: bool
) -> None:
    so = Solution()
    actual = so.exist(board, word)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        )

    def test_2(self):
        test(
            self,
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        )

    def test_3(self):
        test(
            self,
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        )

    def test_4(self):
        test(self, [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB", True)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
5562 ms
Beats
52.29%
"""

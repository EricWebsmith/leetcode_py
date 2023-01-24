import unittest
from collections import deque


def move(position: int, board: list[list[int]]) -> int:
    # if there is a ladder or snake
    # take the ladder or snake
    n = len(board)
    r = n - 1 - (position - 1) // n
    c = (position - 1) % n
    if (n - 1 - r) % 2 == 1:
        c = n - 1 - c

    next_position = board[r][c]
    if next_position != -1:
        return next_position

    # otherwise, do nothing.
    return position


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        seen: set[int] = {1}
        current_positions = deque[tuple[int, int]]()
        current_positions.append((1, 0))
        while len(current_positions) > 0:
            position, steps = current_positions.popleft()
            for next_position in range(position + 1, position + 6 + 1):
                if next_position == n * n:
                    return steps + 1
                final_next_position = move(next_position, board)
                if final_next_position == n * n:
                    return steps + 1
                if final_next_position in seen:
                    continue
                seen.add(final_next_position)
                current_positions.append((final_next_position, steps + 1))

        return -1


def test(testObj: unittest.TestCase, board: list[list[int]], expected: int) -> None:
    so = Solution()
    actual = so.snakesAndLadders(board)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
        )

    def test_2(self):
        test(self, [[-1, -1], [-1, 3]], 1)

    def test_3(self):
        test(self, [[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]], 1)

    def test_4(self):
        test(self, [[1, 1, -1], [1, 1, 1], [-1, 1, 1]], -1)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
118 ms
Beats
82.64%
"""

import unittest
from typing import List


def get_rows(grid: List[List[int]]) -> List[int]:
    m = len(grid)
    n = len(grid[0])
    rows: list = []
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                rows.append(r)
    return rows


def get_cols(grid: List[List[int]]) -> List[int]:
    m = len(grid)
    n = len(grid[0])
    cols: list = []
    for c in range(n):
        for r in range(m):
            if grid[r][c] == 1:
                cols.append(c)
    return cols


def get_dis(arr: List[int]) -> int:
    n = len(arr)
    left = 0
    right = n - 1
    ans = 0
    while left < right:
        ans += arr[right] - arr[left]
        left += 1
        right -= 1
    return ans


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = get_rows(grid)
        cols = get_cols(grid)
        r_ans = get_dis(rows)
        c_ans = get_dis(cols)
        return r_ans + c_ans


def test(testObj: unittest.TestCase, grid: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.minTotalDistance(grid)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 6)

    def test_2(self):
        test(self, [[1, 1]], 1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
149 ms
Beats
79.39%
"""

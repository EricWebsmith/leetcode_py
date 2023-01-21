import unittest


class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        mat = [[0] * n for _ in range(n)]
        for query in queries:
            for r in range(query[0], query[2] + 1):
                # Range Caching for each row
                mat[r][query[1]] += 1
                if query[3] + 1 < n:
                    mat[r][query[3] + 1] -= 1

        for r in range(n):
            prev = 0
            for c in range(n):
                mat[r][c] += prev
                prev = mat[r][c]

        return mat


def test(
    testObj: unittest.TestCase,
    n: int,
    queries: list[list[int]],
    expected: list[list[int]],
) -> None:
    so = Solution()
    actual = so.rangeAddQueries(n, queries)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 3, [[1, 1, 2, 2], [0, 0, 1, 1]], [[1, 1, 0], [1, 2, 1], [0, 1, 1]])

    def test_2(self):
        test(self, 2, [[0, 0, 1, 1]], [[1, 1], [1, 1]])

    def test_3(self):
        self.maxDiff = None
        test(
            self,
            13,
            [
                [3, 1, 7, 3],
                [7, 5, 7, 8],
                [4, 12, 6, 12],
                [2, 8, 6, 11],
                [9, 11, 10, 11],
                [9, 3, 11, 11],
                [0, 12, 10, 12],
                [10, 5, 11, 12],
                [4, 7, 6, 12],
                [0, 2, 9, 6],
                [12, 7, 12, 11],
                [2, 7, 3, 8],
                [2, 9, 6, 12],
                [10, 7, 10, 12],
                [11, 6, 11, 7],
                [3, 2, 12, 9],
            ],
            [
                [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
                [0, 1, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2],
                [0, 1, 3, 3, 2, 2, 2, 2, 3, 4, 3, 3, 4],
                [0, 1, 3, 3, 2, 2, 2, 2, 3, 4, 3, 3, 4],
                [0, 1, 3, 3, 2, 2, 2, 2, 3, 4, 3, 3, 4],
                [0, 1, 3, 3, 2, 3, 3, 2, 2, 1, 0, 0, 1],
                [0, 0, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0, 1],
                [0, 0, 2, 3, 3, 3, 3, 2, 2, 2, 1, 2, 1],
                [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 3, 4, 3],
                [0, 0, 1, 2, 2, 3, 4, 4, 3, 3, 2, 2, 1],
                [0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0],
            ],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime
3292 ms
Beats
55.56%
"""

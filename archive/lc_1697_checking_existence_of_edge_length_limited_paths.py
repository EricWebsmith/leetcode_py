import unittest


class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> int:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1

        if px > py:
            self.p[px] = py
        else:
            self.p[py] = px
        self.e += 1
        return 0


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        edgeList.sort(key=lambda x: -x[2])

        queries = [(s, d, l, i) for i, (s, d, l) in enumerate(queries)]
        queries.sort(key=lambda x: x[2])

        ans = [False] * len(queries)

        dsu = DSU(n)
        for s, d, l, i in queries:
            while edgeList and edgeList[-1][2] < l:
                a, b, _ = edgeList.pop()
                dsu.union(a, b)
            ans[i] = dsu.find(s) == dsu.find(d)

        return ans


def test(
    testObj: unittest.TestCase,
    n: int,
    edgeList: list[list[int]],
    queries: list[list[int]],
    expected: list[bool],
) -> None:
    so = Solution()
    actual = so.distanceLimitedPathsExist(n, edgeList, queries)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            3,
            [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
            [[0, 1, 2], [0, 2, 5]],
            [False, True],
        )

    def test_2(self):
        test(
            self,
            5,
            [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
            [[0, 4, 14], [1, 4, 13]],
            [True, False],
        )


if __name__ == "__main__":
    unittest.main()

# the spelling is mistaken
# Exaplanation

"""
Runtime
2675 ms
Beats
58.61%
"""

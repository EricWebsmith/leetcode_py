import unittest
from typing import List


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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sorted_edges = [(a, b, w, i) for i, (a, b, w) in enumerate(edges)]
        sorted_edges.sort(key=lambda x: x[2])
        dsu = DSU(n)
        mst = 0
        max_weight = 0

        pseudo_critical = set()
        for a, b, w, i in sorted_edges:
            pa = dsu.find(a)
            pb = dsu.find(b)
            if pa == pb:
                continue
            pseudo_critical.add(i)
            dsu.union(pa, pb)
            max_weight = max(max_weight, w)
            mst += w
            if dsu.e == n - 1:
                break

        for pseudo_critical_index in range(len(sorted_edges)):
            if pseudo_critical_index in pseudo_critical:
                continue

            new_mst = 0
            new_dsu = DSU(n)
            a, b, w = edges[pseudo_critical_index]
            if w > max_weight:
                continue
            new_dsu.union(a, b)
            new_mst += w
            for a, b, w, i in sorted_edges:
                if i == pseudo_critical_index:
                    continue
                pa = new_dsu.find(a)
                pb = new_dsu.find(b)
                if pa == pb:
                    continue
                new_dsu.union(pa, pb)
                new_mst += w
                if new_dsu.e == n - 1:
                    break

            if new_dsu.e == n - 1 and new_mst == mst:
                pseudo_critical.add(pseudo_critical_index)

        critical: list = []
        for critical_index in pseudo_critical:
            new_mst = 0
            new_dsu = DSU(n)
            for a, b, w, i in sorted_edges:
                if i == critical_index:
                    continue
                pa = new_dsu.find(a)
                pb = new_dsu.find(b)
                if pa == pb:
                    continue
                new_dsu.union(pa, pb)
                new_mst += w
                if new_dsu.e == n - 1:
                    break

            if new_dsu.e < n - 1 or new_mst > mst:
                critical.append(critical_index)

        for critical_index in critical:
            pseudo_critical.remove(critical_index)

        return [critical, list(pseudo_critical)]


def test(
    testObj: unittest.TestCase,
    n: int,
    edges: List[List[int]],
    expected: List[List[int]],
) -> None:

    so = Solution()

    actual = so.findCriticalAndPseudoCriticalEdges(n, edges)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            5,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
            [[0, 1], [2, 3, 4, 5]],
        )

    def test_2(self):
        test(self, 4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]], [[], [0, 1, 2, 3]])

    def test_3(self):
        test(self, 2, [[0, 1, 1]], [[0], []])


if __name__ == "__main__":
    unittest.main()

# adding max weight has significant impact
# from 2000ms to 1000ms
"""
Runtime: 782 ms, faster than 83.65%
Memory Usage: 14.1 MB, less than 60.58%
"""

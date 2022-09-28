import unittest
from typing import List
from collections import defaultdict, Counter


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
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        uf = DSU(n)
        e = defaultdict(list)
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)

        value_indices = defaultdict(list)
        for i, v in enumerate(vals):
            value_indices[v].append(i)

        ans = n
        for v in sorted(value_indices.keys()):
            for i in value_indices[v]:
                for j in e[i]:
                    if vals[j] <= v:
                        uf.union(i, j)

            c = Counter()
            for i in value_indices[v]:
                p = uf.find(i)
                c[p] += 1

            for _, count in c.items():
                if count > 1:
                    ans += count * (count - 1) // 2

        return ans


def test(testObj: unittest.TestCase, vals: List[int], edges: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.numberOfGoodPaths(vals, edges)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3, 2, 1, 3],  [[0, 1], [0, 2], [2, 3], [2, 4]], 6)

    def test_2(self):
        test(self,   [1, 1, 2, 2, 3],  [[0, 1], [1, 2], [2, 3], [2, 4]], 7)

    def test_3(self):
        test(self,   [1],  [], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 2031 ms, faster than 69.23% of Python3 online submissions for Number of Good Paths.
Memory Usage: 31.9 MB, less than 38.46% of Python3 online submissions for Number of Good Paths.
'''

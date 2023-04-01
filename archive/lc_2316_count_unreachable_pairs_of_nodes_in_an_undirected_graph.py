import unittest
from collections import defaultdict


class DSU:
    def __init__(self, n: int) -> None:
        self.union_find = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x != self.union_find[x]:
            self.union_find[x] = self.find(self.union_find[x])
        return self.union_find[x]

    def union(self, x: int, y: int) -> int:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1

        if px > py:
            self.union_find[px] = py
        else:
            self.union_find[py] = px
        self.e += 1
        return 0


class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        dsu = DSU(n)
        for [u, v] in edges:
            dsu.union(u, v)

        for i in range(n):
            dsu.find(i)
        
        d: dict[int, int] = defaultdict(lambda : 0)
        for group in dsu.union_find:
            d[group] += 1

        ans = 0
        for v in d.values():
            ans += v * (n - v)
        
        return ans // 2


def test(testObj: unittest.TestCase, n: int, edges: list[list[int]], expected: int) -> None:
    so = Solution()
    actual = so.countPairs(n, edges)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   3,  [[0,1],[0,2],[1,2]], 0)

    def test_2(self):
        test(self,   7,  [[0,2],[0,5],[2,4],[1,6],[5,4]], 14)

    def test_3(self):
        test(self, 11, [[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]], 0)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
2212 ms
Beats
56.94%
'''

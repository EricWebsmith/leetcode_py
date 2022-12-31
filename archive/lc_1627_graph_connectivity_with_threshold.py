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

    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:

        if threshold == 0:
            return [True]*len(queries)

        dsu = DSU(n+1)
        for i in range(threshold + 1, n+1):
            for j in range(2*i, n+1, i):
                dsu.union(i, j)

        return [dsu.find(i) == dsu.find(j) for i, j in queries]


def test(testObj: unittest.TestCase, n: int, threshold: int, queries: list[list[int]], expected: list[bool]) -> None:
    so = Solution()
    actual = so.areConnected(n, threshold, queries)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   6,  2,  [[1, 4], [2, 5], [3, 6]], [False, False, True])

    def test_2(self):
        test(self,   6,  0,  [[4, 5], [3, 4], [3, 2], [
             2, 6], [1, 3]], [True, True, True, True, True])

    def test_3(self):
        test(self,   5,  1,  [[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]],
             [False, False, False, False, False])

    def test_4(self):
        test(self,   14,  4,
             [[4, 2], [7, 2], [4, 3], [1, 4], [4, 11], [6, 8], [8, 12], [12, 5], [3, 7], [12, 6], [3, 6],
              [11, 9], [6, 9], [6, 4], [4, 9], [14, 4], [10, 14], [14, 2], [9, 8], [8, 7], [13, 14],
              [12, 4], [7, 4], [10, 4], [1, 6], [9, 7], [5, 13], [10, 11], [14, 8], [5, 6], [7, 12],
              [11, 5], [8, 13], [4, 8], [1, 9], [8, 2], [1, 13], [5, 9], [12, 1], [13, 10], [1, 8],
              [10, 6], [9, 13], [6, 11], [3, 5], [5, 2]],
             [False, False, False, False, False, False, False, False, False, True, False, False, False,
              False, False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 875 ms, faster than 99.32%
Memory Usage: 48.9 MB, less than 95.92%
'''

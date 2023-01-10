import unittest
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p: list = []
        for i in range(m):
            p.append(i+1)

        ans: list = []
        for q in queries:
            i = p.index(q)
            ans.append(i)
            p = [p[i]]+p[:i]+p[i+1:]

        return ans


def test(testObj: unittest.TestCase, queries: List[int], m: int, expected: int) -> None:

    so = Solution()
    actual = so.processQueries(queries, m)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 1, 2, 1],  5, [2, 1, 2, 1])

    def test_2(self):
        test(self,   [4, 1, 2, 2],  4, [3, 1, 2, 0])

    def test_3(self):
        test(self,   [7, 5, 5, 8, 3],  8, [6, 5, 0, 7, 5])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 93 ms, faster than 69.50%
Memory Usage: 14.1 MB, less than 47.52%
'''

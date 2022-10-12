import unittest
from functools import cache


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 1_000_000_007

        @cache
        def dfs(n, k):
            if n == k:
                return 1

            if n < k:
                return 0

            if k == 0 or n == 0:
                return 0

            return (dfs(n-1, k-1) + (n-1)*dfs(n-1, k)) % MOD

        return dfs(n, k) % MOD


def test(testObj: unittest.TestCase, n: int, k: int, expected: int) -> None:

    so = Solution()

    actual = so.rearrangeSticks(n, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   3,  2, 3)

    def test_2(self):
        test(self,   5,  5, 1)

    def test_3(self):
        test(self,   20,  11, 647427950)

    def test_4(self):
        test(self,   4,  2, 11)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
2222 ms
Beats
87.69%
'''

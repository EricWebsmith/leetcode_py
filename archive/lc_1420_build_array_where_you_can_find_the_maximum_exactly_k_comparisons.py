import itertools
import unittest


def choose(n, k):
    ans = 1
    for i in range(k):
        ans *= (n-i) // (i+1)
    return ans


class Solution:
    def numOfArrays(self, N: int, M: int, K: int) -> int:
        dp = [[[0 for _ in range(M + 1)] for _ in range(K + 1)]
              for _ in range(N + 1)]

        for k in range(1, M + 1):
            dp[1][1][k] = 1

        for i, j, k in itertools.product(range(1, N + 1), range(1, K + 1), range(M + 1)):
            dp[i][j][k] += dp[i - 1][j][k] * k
            dp[i][j][k] += sum(dp[i - 1][j - 1][1:k])

        return sum(dp[N][K][1:]) % (10 ** 9 + 7)


def test(testObj: unittest.TestCase, n: int, m: int, k: int, expected: int) -> None:
    so = Solution()
    actual = so.numOfArrays(n, m, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   2,  3,  1, 6)

    def test_2(self):
        test(self,   5,  2,  3, 0)

    def test_3(self):
        test(self,   9,  1,  1, 1)

    def test_4(self):
        test(self,   50,  100,  10, 329962470)

    def test_5(self):
        test(self,   2,  3,  2, 3)

    def test_6(self):
        test(self,   3,  4,  2, 30)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
386 ms
Beats
92.65%
'''

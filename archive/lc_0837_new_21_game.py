import unittest


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k - 1 + maxPts <= n:
            return 1

        dp: list[float] = [0] * (k + maxPts)
        for i in range(k, n + 1):
            dp[i] = 1

        s = (n - k + 1) / maxPts
        for i in range(k - 1, -1, -1):
            dp[i] = s
            s -= dp[i + maxPts] / maxPts
            s += dp[i] / maxPts

        return dp[0]


def test(testObj: unittest.TestCase, n: int, k: int, maxPts: int, expected: float) -> None:
    so = Solution()
    actual = so.new21Game(n, k, maxPts)
    testObj.assertAlmostEqual(actual, expected, delta=0.0001)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 10, 1, 10, 1.00000)

    def test_2(self):
        test(self, 6, 1, 10, 0.60000)

    def test_3(self):
        test(self, 21, 17, 10, 0.73278)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
63 ms
Beats
99.47%
"""

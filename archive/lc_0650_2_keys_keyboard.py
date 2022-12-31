
import unittest
from math import sqrt

# dp = [n] * (n+1)
# dp[0] = 0
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 4
# dp[5] = 5
# dp[6] = dp[3] + 2
# dp[7] = 7
# dp[8] = dp[4] + 2
# dp[9] = dp[3] + 3
# dp[10] = dp[5] + 2
# dp[11] = 11


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        if n <= 5:
            return n

        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return self.minSteps(n//i) + i

        return n


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()
    actual = so.minSteps(n)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,   3, 3)

    def test_2(self):
        test(self,   1, 0)

    def test_3(self):
        test(self,   11, 11)

    def test_4(self):
        test(self,   100, 14)

    def test_5(self):
        test(self,   1000, 21)


if __name__ == '__main__':
    unittest.main()

"""
Runtime: 49 ms, faster than 80.46%
Memory Usage: 14 MB, less than 41.37%
"""

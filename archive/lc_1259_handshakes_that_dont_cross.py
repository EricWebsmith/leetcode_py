import unittest


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 1_000_000_007
        dp = [1, 1]
        for i in range(2, numPeople//2+1):
            t = 0
            j = 0
            while j < i-j-1:
                t += dp[j] * dp[i-j-1] * 2
                t %= MOD
                j += 1

            if j == i-j-1:
                t += dp[j] * dp[j]
                t %= MOD
            dp.append(t)

        return dp[-1]


def test(testObj: unittest.TestCase, numPeople: int, expected: int) -> None:

    so = Solution()

    actual = so.numberOfWays(numPeople)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_2(self):
        test(self,   2, 1)

    def test_4(self):
        test(self,   4, 2)

    def test_6(self):
        test(self,   6, 5)

    def test_8(self):
        test(self,   8, 14)

    def test_10(self):
        test(self,   10, 42)

    def test_12(self):
        test(self,   12, 132)

    def test_14(self):
        test(self,   14, 429)

    def test_100(self):
        test(self,   100, 265470434)

    def test_128(self):
        test(self,   128, 887145589)

    def test_1000(self):
        test(self,   1000, 591137401)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 574 ms, faster than 90.00%
Memory Usage: 13.8 MB, less than 98.89%
'''

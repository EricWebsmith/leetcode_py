import unittest


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] * (len(s) + 1)
        for ti in range(len(t)):

            new_dp = [0] * (len(s) + 1)
            for si in range(len(s)):
                if s[si] == t[ti]:
                    new_dp[si + 1] = new_dp[si] + dp[si]
                else:
                    new_dp[si + 1] = new_dp[si]

            dp = new_dp

        return dp[-1]


def test(testObj: unittest.TestCase, s: str, t: str, expected: int) -> None:

    so = Solution()

    actual = so.numDistinct(s, t)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "rabbbit", "rabbit", 3)

    def test_2(self):
        test(self, "babgbag", "bag", 5)

    def test_3(self):
        test(self, "ab", "ab", 1)

    def test_4(self):
        test(self, "rabbbbit", "rabbit", 6)

    def test_5(self):
        test(self, "rabbbbbit", "rabbit", 10)

    def test_6(self):
        test(self, "raabbbit", "rabbit", 6)

    def test_7(self):
        test(self, "raabbbit", "abc", 0)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 487 ms, faster than 88.52%
Memory Usage: 14.2 MB, less than 92.89%
"""

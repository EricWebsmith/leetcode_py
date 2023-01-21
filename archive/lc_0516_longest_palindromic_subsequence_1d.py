import unittest


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for r in range(n):
            next_dp = [0] * (n + 1)
            for c in range(n):
                if s[c] == s[n - r - 1]:
                    next_dp[c + 1] = dp[c] + 1
                else:
                    next_dp[c + 1] = max(dp[c + 1], next_dp[c])
            dp = next_dp
        return dp[-1]


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()

    actual = so.longestPalindromeSubseq(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "bbbab", 4)

    def test_2(self):
        test(self, "cbbd", 2)

    def test_3(self):
        test(self, "abcd", 1)

    def test_4(self):
        test(self, "abcdcba", 7)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 2451 ms, faster than 61.17%
Memory Usage: 13.9 MB, less than 95.48%
"""

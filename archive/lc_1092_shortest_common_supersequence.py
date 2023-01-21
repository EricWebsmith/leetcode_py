import unittest


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for r in range(m):
            for c in range(n):
                if str1[r] == str2[c]:
                    dp[r + 1][c + 1] = dp[r][c] + 1
                else:
                    dp[r + 1][c + 1] = max(dp[r][c + 1], dp[r + 1][c])

        # traceback
        r = m
        c = n
        t = ""
        while (r > 0) or (c > 0):
            if r > 0 and c > 0 and str1[r - 1] == str2[c - 1]:
                t = str1[r - 1] + t
                r -= 1
                c -= 1
            elif r == 0 or (c > 0 and dp[r][c - 1] == dp[r][c]):
                t = str2[c - 1] + t
                c -= 1
            else:
                t = str1[r - 1] + t
                r -= 1

        return t


def is_sub(s: str, sub: str):
    sub_i = 0
    for i in range(len(s)):
        if s[i] == sub[sub_i]:
            sub_i += 1
        if sub_i == len(sub):
            return True
    return sub_i == len(sub)


def test(testObj: unittest.TestCase, str1: str, str2: str, expected: str) -> None:

    so = Solution()

    actual = so.shortestCommonSupersequence(str1, str2)
    testObj.assertTrue(is_sub(actual, str1))
    testObj.assertTrue(is_sub(actual, str2))
    testObj.assertEqual(len(actual), len(expected))


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "abac", "cab", "cabac")

    def test_2(self):
        test(self, "aaaaaaaa", "aaaaaaaa", "aaaaaaaa")

    def test_3(self):
        test(self, "aceb", "abcab", "abceab")

    def test_4(self):
        test(self, "a", "b", "ab")

    def test_5(self):
        test(self, "abc", "bcd", "abcd")

    def test_6(self):
        test(
            self,
            "bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb",
            "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa",
            "dddbbdcaabccaccbababaacbdcbacddadcdacbadcaddcdcccdbacdadcbabdaccbccdbaaacdcbcaccacbbdacbabb",
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 419 ms, faster than 97.50%
Memory Usage: 21.8 MB, less than 94.87%
"""

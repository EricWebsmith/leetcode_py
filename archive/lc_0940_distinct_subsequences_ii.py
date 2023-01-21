import unittest


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 1_000_000_007
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = [0] * 26
        for i in range(1, n + 1):
            char_index = ord(s[i - 1]) - ord("a")
            j = last[char_index]
            dup = dp[j - 1] if j > 0 else 0
            dp[i] = ((dp[i - 1] << 1) - dup) % mod
            last[char_index] = i

        return (dp[-1] - 1) % mod


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()
    actual = so.distinctSubseqII(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "abc", 7)

    def test_2(self):
        test(self, "aba", 6)

    def test_3(self):
        test(self, "aaa", 3)

    def test_4(self):
        test(self, "lee", 5)

    def test_5(self):
        test(
            self,
            "zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn",
            97915677,
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime
47 ms
Beats
98.75%
"""

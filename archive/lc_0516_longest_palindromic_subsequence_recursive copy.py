import unittest


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = list(list(-1 for _ in range(len(s))) for _ in range(len(s)))

        def dp(left, right) -> int:
            if left > right:
                return 0
            if memo[left][right] != -1:
                return memo[left][right]
            else:
                if left == right:
                    ret = 1
                else:
                    if s[left] == s[right]:
                        ret = dp(left+1, right-1) + 2
                    else:
                        ret = max(dp(left+1, right), dp(left, right-1))
                memo[left][right] = ret
                return ret

        return dp(0, len(s)-1)


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:
    so = Solution()
    actual = so.longestPalindromeSubseq(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "bbbab", 4)

    def test_2(self):
        test(self,   "cbbd", 2)

    def test_3(self):
        test(self,   "abcd", 1)

    def test_4(self):
        test(self,   "abcdcba", 7)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 3418 ms, faster than 42.26%
Memory Usage: 79.1 MB, less than 24.08%
'''

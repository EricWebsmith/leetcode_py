import unittest
from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def dp(left, right) -> int:
            if left > right:
                return 0, None
            elif left == right:
                return 0, None
            else:
                if s[left] == s[right] and s[left]:
                    count, c = dp(left+1, right-1)
                    if c == s[left]:
                        return count, c
                    else:
                        return count+2, s[left]
                else:
                    left_count, left_c = dp(left+1, right)
                    right_count, right_c = dp(left, right-1)
                    if left_count > right_count:
                        return left_count, left_c
                    elif right_count > left_count:
                        return right_count, right_c
                    elif left_c == right_c:
                        return right_count, right_c
                    else:
                        return right_count, None

        return dp(0, len(s)-1)[0]


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()

    actual = so.longestPalindromeSubseq(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "bbabab", 4)

    def test_2(self):
        test(self,   "dcbccacdb", 4)

    def test_3(self):
        test(self,   "baad", 2)

    def test_4(self):
        test(self,   "aba", 2)

    def test_5(self):
        test(self,   "udpdjnmlcekqctotjaaqeuikbknoqhrjzwdivybtqtjjelzeveruwudebsbemoaetdfuoagrkaoyotidhvwmworkwlguyvebixyarkvxoglbfctcjjschtyomaxdcnumqdcouwjwdbdcrwsvjfjdavibjkkxcsrdqvmjxmhhnmxtnglawnhtvlgwcrfxitvesalreuvkzrtkyyptkvwrwavocnhdmrjvtzqedvzigoybqgyjh", 80)  # noqa

    def test_6(self):
        test(self,   "hnkzqnijsjwetjsjzhqqxyecqrjbuaxifhgilqgchkiynkzpcymqxwgntacusvjmxfqslchsdvapolduzogkjjnsgqmkgxdrkcejubclkvcinpbpibzkgmraxnxmxnkrlfqljtfhztradlmrlwytphgkbeyflyfxojxaqbhqwdahxwifuvcwtkplzjyhuzevsdmsritmhwwanilvzgbcayzctsldimhnesppju", 74)  # noqa


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 315 ms, faster than 95.29%
Memory Usage: 85.4 MB, less than 58.82%
'''

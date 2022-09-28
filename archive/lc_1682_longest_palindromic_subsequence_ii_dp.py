from functools import cache
import unittest
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def dp(l, r) -> int:
            if l > r:
                return 0, None
            elif l == r:
                return 0, None
            else:
                if s[l] == s[r] and s[l]:
                    count, c = dp(l+1, r-1)
                    if c == s[l]:
                        return count, c
                    else:
                        return count+2, s[l]
                else:
                    left_count, left_c = dp(l+1, r)
                    right_count, right_c = dp(l, r-1)
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
        test(self,   "udpdjnmlcekqctotjaaqeuikbknoqhrjzwdivybtqtjjelzeveruwudebsbemoaetdfuoagrkaoyotidhvwmworkwlguyvebixyarkvxoglbfctcjjschtyomaxdcnumqdcouwjwdbdcrwsvjfjdavibjkkxcsrdqvmjxmhhnmxtnglawnhtvlgwcrfxitvesalreuvkzrtkyyptkvwrwavocnhdmrjvtzqedvzigoybqgyjh", 80)

    def test_6(self):
        test(self,   "hnkzqnijsjwetjsjzhqqxyecqrjbuaxifhgilqgchkiynkzpcymqxwgntacusvjmxfqslchsdvapolduzogkjjnsgqmkgxdrkcejubclkvcinpbpibzkgmraxnxmxnkrlfqljtfhztradlmrlwytphgkbeyflyfxojxaqbhqwdahxwifuvcwtkplzjyhuzevsdmsritmhwwanilvzgbcayzctsldimhnesppju", 74)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 315 ms, faster than 95.29% of Python3 online submissions for Longest Palindromic Subsequence II.
Memory Usage: 85.4 MB, less than 58.82% of Python3 online submissions for Longest Palindromic Subsequence II.
'''

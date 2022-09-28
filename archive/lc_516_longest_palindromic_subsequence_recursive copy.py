import unittest
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = list(list(-1 for _ in range(len(s))) for _ in range(len(s)))
        
        def dp(l,r) -> int:
            if l > r:
                return 0
            if memo[l][r] != -1:
                return memo[l][r]
            else:
                if l == r:
                    ret = 1
                else:
                    if s[l] == s[r]:
                        ret = dp(l+1,r-1) + 2
                    else:
                        ret = max(dp(l+1,r),dp(l,r-1))
                memo[l][r] = ret
                return ret
        
        return dp(0,len(s)-1)



def test(testObj: unittest.TestCase, s: str, expected:int) -> None:
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
Runtime: 3418 ms, faster than 42.26% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 79.1 MB, less than 24.08% of Python3 online submissions for Longest Palindromic Subsequence.
'''

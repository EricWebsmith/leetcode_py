import unittest
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        2D DP, Simple but slow.
        """
        n = len(s)
        dp = [[0] * (n+1) for i in range(n+1)]
        t = list(s)
        t.reverse()
        for r in range(n):
            for c in range(n):
                if s[c] == t[r]:
                    dp[r+1][c+1] = dp[r][c] + 1
                else:
                    dp[r+1][c+1] = max(dp[r][c+1], dp[r+1][c])
        
        return dp[-1][-1]



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
Runtime: 7791 ms, faster than 5.03% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 39.2 MB, less than 44.75% of Python3 online submissions for Longest Palindromic Subsequence.
'''

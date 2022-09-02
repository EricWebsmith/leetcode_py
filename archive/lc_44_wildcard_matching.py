from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p == "":
            return True
        if p == "" and s != "":
            return False
        while '**' in p:
            p = p.replace('**', '*')
        dp = [False] * (len(p)+1)
        dp[0] = True
        if p[0] == '*':
            dp[1] = True

        for r in range(len(s)):
            current = [False] * (len(p)+1)
            for c in range(len(p)):
                if s[r] == p[c] or p[c] == '?':
                    current[c+1] = dp[c]
                elif p[c] == '*':
                    current[c+1] = dp[c] or dp[c+1] or current[c]
            dp = current

        return dp[-1]


def test(testObj: unittest.TestCase, s: str, p: str, expected: int) -> None:

    so = Solution()
    actual = so.isMatch(s, p)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "aa",  "a", False)

    def test_2(self):
        test(self,   "aa",  "*", True)

    def test_3(self):
        test(self,   "cb",  "?a", False)

    def test_4(self):
        test(self,   "adceb", "*a*b", True)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 449 ms, faster than 82.36% of Python3 online submissions for Wildcard Matching.
Memory Usage: 13.9 MB, less than 97.28% of Python3 online submissions for Wildcard Matching.
'''

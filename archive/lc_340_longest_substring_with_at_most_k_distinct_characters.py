from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from queue import Queue
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        if n<=k:
            return n

        left = 0
        right = 0
        d = {}
        while right<n and len(d)<k:
            d[s[right]] = right
            right+=1

        max_length = right - left
        while right<n:
            if not s[right] in d:
                remove_char = ''
                earliest = right
                for k, v in d.items():
                    if v<earliest:
                        remove_char = k
                        earliest = v
                left = earliest + 1
                del d[remove_char]
            max_length = max(max_length, right-left+1)
            d[s[right]] = right
            right += 1

        return max_length


def test(testObj: unittest.TestCase, s: str, k: int, expected:int) -> None:
    
    so = Solution()
    actual = so.lengthOfLongestSubstringKDistinct(s,k)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   "eceba",  2, 3)

    def test_2(self):
        test(self,   "aa",  1, 2)
    
    def test_3(self):
        test(self,   "aabcdqfasdf",  20, 11)
    
    def test_4(self):
        test(self,   "ababababab",  2, 10)
    
    def test_5(self):
        test(self,   "abcabcabcd",  3, 9)
    
    def test_6(self):
        test(self,   "aa",  0, 0)
    
    def test_7(self):
        test(self,   "ab",  1, 1)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 76 ms, faster than 94.26% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
Memory Usage: 14.3 MB, less than 42.46% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
'''

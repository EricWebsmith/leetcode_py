
from collections import defaultdict
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        d = defaultdict(int)

        for start, end, direction in shifts:
            if direction == 0:
                d[start] -= 1
                d[end+1] += 1                    
            else:
                d[start] += 1
                d[end+1] -= 1

        cum_sum = 0
        ans = ''
        for i in range(n):
            cum_sum += d[i]
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            ans += chr(new_code)
        return ans


def test(testObj: unittest.TestCase, s: str, shifts: List[List[int]], expected:int) -> None:
    
    so = Solution()
    actual = so.shiftingLetters(s,shifts)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  "abc",  [[0,1,0],[1,2,1],[0,2,1]], "ace")

    def test_2(self):
        test(self,  "dztz",  [[0,0,0],[1,1,1]], "catz")
    

if __name__ == '__main__':
    unittest.main()
        
"""
Runtime: 2239 ms, faster than 80.00% of Python3 online submissions for Shifting Letters II.
Memory Usage: 42.9 MB, less than 40.00% of Python3 online submissions for Shifting Letters II.
"""
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
import re

class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        s = list(s)
        index = n - 1
        start_removing = False
        end = -1
        stars = 0
        while index>=0:
            if s[index] == '*':
                start_removing = True
                if end == -1:
                    end = index
                stars+=1
            elif start_removing:
                stars-=1

            if start_removing and stars==0 and (index>0 and s[index-1]!='*' or index == 0):
                t = []
                if index>0:
                    t += s[:index]
                if end<n-1:
                    t += s[end+1:]
                s = t
                start_removing = False
                stars = 0
                end = -1

            
            index-=1
        return "".join(s)


def test(testObj: unittest.TestCase, s: str, expected:int) -> None:
    
    so = Solution()
    actual = so.removeStars(s)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   "leet**cod*e", "lecoe")

    def test_2(self):
        test(self,   "erase*****", "")
    

if __name__ == '__main__':
    unittest.main()

'''

'''


from heapq import heappop, heappush
import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s_index = -1
        flip = 1
        for t_index in range(len(target)):
            s_index+=1
            if s_index == len(source):
                s_index = 0
                flip += 1

            while s_index < len(source) and target[t_index] != source[s_index]:
                s_index+=1
            
            if s_index ==  len(source):
                flip+=1
                s_index = 0
                while s_index < len(source) and target[t_index] != source[s_index]:
                    s_index+=1
                if s_index == len(source):
                    return -1

        return flip


def test(testObj: unittest.TestCase, source: str, target: str, expected:int) -> None:
    
    so = Solution()
    actual = so.shortestWay(source,target)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,   "abc",  "abcbc", 2)

    def test_2(self):
        test(self,   "abc",  "acdbc", -1)

    def test_3(self):
        test(self,   "xyz",  "xzyxz", 3)
    
    def test_4(self):
        test(self,   "aaaaa", "aaaaaaaaaaaaa", 3)
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 73 ms, faster than 54.60% of Python3 online submissions for Shortest Way to Form String.
Memory Usage: 14 MB, less than 43.14% of Python3 online submissions for Shortest Way to Form String.
"""
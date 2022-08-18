
from heapq import heappop, heappush
import unittest
from typing import List, Optional
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from nary_tree import Node, array_to_node, node_to_array


class Solution:
    def cloneTree(self, root: Node) -> Node:
        if root is None:
            return None

        newRoot = Node(root.val)
        for child in root.children:
            newRoot.children.append(self.cloneTree(child))

        return newRoot


def test(testObj: unittest.TestCase, rootArr: Node, expected:int) -> None:
    root = array_to_node(rootArr)
    s = Solution()
    actualRoot = s.cloneTree(root)
    actual = node_to_array(actualRoot)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  [1,None,3,2,4,None,5,6], [1,None,3,2,4,None,5,6])

    def test_2(self):
        test(self,  [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14], [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
    

if __name__ == '__main__':
    unittest.main()
        
"""
Runtime: 106 ms, faster than 78.43% of Python3 online submissions for Clone N-ary Tree.
Memory Usage: 17.9 MB, less than 79.88% of Python3 online submissions for Clone N-ary Tree.
"""        
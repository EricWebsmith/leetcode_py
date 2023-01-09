from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
from data_structure.link_list import ListNode, listnode_to_array, array_to_listnode
null = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        pass



def test(testObj: unittest.TestCase, l1_arr: List[int], l2_arr: List[int], expected:Optional[ListNode]) -> None:
    l1 = array_to_listnode(l1_arr)
    l2 = array_to_listnode(l2_arr)
    so = Solution()
    
    actual_root = so.addTwoNumbers(l1,l2)
    actual = listnode_to_array(actual_root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [2,4,3],  [5,6,4], [7,0,8])

    def test_2(self):
        test(self,   [0],  [0], [0])

    def test_3(self):
        test(self,   [9,9,9,9,9,9,9],  [9,9,9,9], [8,9,9,9,0,0,0,1])


if __name__ == '__main__':
    unittest.main()

'''

'''

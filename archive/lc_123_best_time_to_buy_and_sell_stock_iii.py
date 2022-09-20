from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        pass



def test(testObj: unittest.TestCase, prices: List[int], expected:int) -> None:
    
    so = Solution()
    
    actual = so.maxProfit(prices)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [3,3,5,0,0,3,1,4], 6)

    def test_2(self):
        test(self,   [1,2,3,4,5], 4)

    def test_3(self):
        test(self,   [7,6,4,3,1], 0)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1393 ms, faster than 89.20% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 28.9 MB, less than 52.29% of Python3 online submissions for Best Time to Buy and Sell Stock III.
'''

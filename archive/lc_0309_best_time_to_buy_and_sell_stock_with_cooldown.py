from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from queue import Queue
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        def dfs(i, buying):
            if i >= n:
                return 0

            if (i, buying) in cache:
                return cache[(i, buying)]

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                cache[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                cache[(i, buying)] = max(sell, cooldown)
            return cache[(i, buying)]
        
        return dfs(0, True)


def test(testObj: unittest.TestCase, prices: List[int], expected:int) -> None:
    
    so = Solution()
    actual = so.maxProfit(prices)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,2,3,0,2], 3)

    def test_2(self):
        test(self,   [1], 0)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 43 ms, faster than 95.53% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 17.8 MB, less than 40.11% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
'''

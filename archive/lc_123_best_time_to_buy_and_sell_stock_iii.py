from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from queue import Queue
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 2
        n = len(prices)
        dp = [[0] * n for i in range(m+1)]

        for r in range(1, m+1):
            max_profit = -prices[0]
            for c in range(1, n):
                dp[r][c] = max(dp[r][c-1], prices[c] + max_profit)
                max_profit = max(max_profit, dp[r-1][c] - prices[c])

        return dp[-1][-1]


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
Runtime: 1745 ms, faster than 72.34% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 28.7 MB, less than 73.35% of Python3 online submissions for Best Time to Buy and Sell Stock III.
'''

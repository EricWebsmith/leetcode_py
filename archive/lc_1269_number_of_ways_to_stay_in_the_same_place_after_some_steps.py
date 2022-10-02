import unittest
from codecs import escape_encode
from collections import defaultdict, deque
from functools import cache, lru_cache
from heapq import heappop, heappush
from math import sqrt
from typing import Any, Dict, List, Optional, Set

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)
from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)
from data_structure.nary_tree import Node, array_to_node, node_to_array

null = None

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dfs(start, num_steps):
            if start<0 or start >= arrLen:
                return 0
            
            if num_steps == 0:
                return start == 0
            
            if start == num_steps:
                return 1
            
            if num_steps<start:
                return 0
            
            return dfs(start+1, num_steps-1) + dfs(start-1, num_steps-1) + dfs(start, num_steps-1)

        return dfs(0, steps) % 1_000_000_007



def test(testObj: unittest.TestCase, steps: int, arrLen: int, expected:int) -> None:
    
    so = Solution()
    
    actual = so.numWays(steps,arrLen)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   3,  2, 4)

    def test_2(self):
        test(self,   2,  4, 2)

    def test_3(self):
        test(self,   4,  2, 8)
    

if __name__ == '__main__':
    unittest.main()

'''
262ms, 91.6%
'''

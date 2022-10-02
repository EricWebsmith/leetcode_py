import unittest
from collections import defaultdict, deque
from functools import cache
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
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for r in range(m-2):
            for c in range(n-2):
                area = grid[r][c] + grid[r][c+1] + grid[r][c+2]
                area += grid[r+1][c+1]
                area += grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
                ans = max(ans, area)

        return ans


def test(testObj: unittest.TestCase, grid: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.maxSum(grid)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[6, 2, 1, 3], [4, 2, 1, 5],
             [9, 2, 8, 7], [4, 1, 2, 9]], 30)

    def test_2(self):
        test(self,   [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 35)

    def test_3(self):
        test(self,   [[6, 2, 1, 3], [4, 2, 1, 5],
             [9, 2, 8, 7], [4, 1, 2, 100]], 119)


    def test_4(self):
        test(self,   [[520626,685427,788912,800638,717251,683428],[23602,608915,697585,957500,154778,209236],[287585,588801,818234,73530,939116,252369]], 5095181)


if __name__ == '__main__':
    unittest.main()

'''

'''

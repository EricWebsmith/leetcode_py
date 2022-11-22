import unittest
from collections import defaultdict, deque
from functools import cache
from heapq import heappop, heappush
from math import ceil, sqrt
from typing import Any, Dict, List, Optional, Set

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)
from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)
from data_structure.nary_tree import Node, array_to_node, node_to_array

null = None


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        rt = ceil(sqrt(n))
        for i in range(2, rt+1):
            s = i * i
            if s > n:
                break
            dp[s] = 1
            for j in range(s+1, n+1):
                dp[j] = min(dp[j], dp[j-s]+1)

        return dp[n]


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:
    so = Solution()
    actual = so.numSquares(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   12, 3)

    def test_2(self):
        test(self,   13, 2)

    def test_3(self):
        test(self,   100, 1)

    def test_4(self):
        test(self,   900, 1)

    def test_5(self):
        test(self,   10000, 1)

    def test_6(self):
        test(self,   1834, 3)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
6093 ms
Beats
16.30%
'''

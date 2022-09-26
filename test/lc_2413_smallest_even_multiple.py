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
    def smallestEvenMultiple(self, n: int) -> int:

        pass


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:
    so = Solution()
    actual = so.smallestEvenMultiple(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   5, 10)

    def test_2(self):
        test(self,   6, 6)


if __name__ == '__main__':
    unittest.main()

'''

'''

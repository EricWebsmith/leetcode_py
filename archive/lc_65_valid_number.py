import re
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match("^[-+]?(\\d+|\\.\\d+|\\d+\\.\\d+|\\d+\\.)([eE][-+]?\\d+)?$", s) is not None


def test(testObj: unittest.TestCase, s: str, expected: bool) -> None:

    so = Solution()

    actual = so.isNumber(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "0", True)

    def test_2(self):
        test(self,   "e", False)

    def test_3(self):
        test(self,   ".", False)

    def test_4(self):
        test(self,   ".1", True)

    def test_5(self):
        test(self,   "+.8", True)

    def test_6(self):
        test(self,   "005047e+6", True)


if __name__ == '__main__':
    unittest.main()

'''

'''
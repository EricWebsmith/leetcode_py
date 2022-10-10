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
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        ans = [pref[0]]
        for i in range(1, n):
            ans.append(pref[i-1] ^ 0 ^ pref[i])

        return ans


def test(testObj: unittest.TestCase, pref: List[int], expected: List[int]) -> None:
    so = Solution()
    actual = so.findArray(pref)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [5, 2, 0, 3, 1], [5, 7, 2, 3, 2])

    def test_2(self):
        test(self,   [13], [13])


if __name__ == '__main__':
    unittest.main()

'''

'''

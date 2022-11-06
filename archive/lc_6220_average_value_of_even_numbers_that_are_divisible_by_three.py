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
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        c = 0
        for num in nums:
            if num % 6 == 0:
                s += num
                c += 1

        return s // c if c > 0 else 0


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()

    actual = so.averageValue(nums)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3, 6, 10, 12, 15], 9)

    def test_2(self):
        test(self,   [1, 2, 4, 7, 10], 0)


if __name__ == '__main__':
    unittest.main()

'''

'''

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
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        ans = [0] * n
        ans_index = 0
        for i in range(n):
            if nums[i] != 0:
                ans[ans_index] = nums[i]
                ans_index += 1

        return ans


def test(testObj: unittest.TestCase, nums: List[int], expected: List[int]) -> None:

    so = Solution()

    actual = so.applyOperations(nums)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0])

    def test_2(self):
        test(self,   [0, 1], [1, 0])


if __name__ == '__main__':
    unittest.main()

'''

'''

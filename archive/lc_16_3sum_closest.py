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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 1_000_000_000
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = n - 1
            while (l < r):
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < abs(diff):
                    diff = target - s
                if s < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0:
                break
        return target - diff


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected: int) -> None:

    so = Solution()

    actual = so.threeSumClosest(nums, target)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [-1, 2, 1, -4],  1, 2)

    def test_2(self):
        test(self,   [0, 0, 0],  1, 0)


if __name__ == '__main__':
    unittest.main()

'''

'''

from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best_val = -1
        best_dis = 1_000_000

        current = root
        while current:
            dis = current.val - target
            abs_dis = abs(current.val - target)
            if abs_dis < best_dis:
                best_dis = abs_dis
                best_val = current.val

            if dis > 0:
                current = current.left
            else:
                current = current.right

        return best_val


def test(testObj: unittest.TestCase, root_arr: List[int], target: float, expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()

    actual = so.closestValue(root, target)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [4, 2, 5, 1, 3],  3.714286, 4)

    def test_2(self):
        test(self,   [1],  4.428571, 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 57 ms, faster than 65.16% of Python3 online submissions for Closest Binary Search Tree Value.
Memory Usage: 16.2 MB, less than 34.57% of Python3 online submissions for Closest Binary Search Tree Value.
'''

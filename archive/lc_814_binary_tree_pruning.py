from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_removable(node: TreeNode):
            if node is None:
                return True
            if node.left is None and node.right is None:
                return node.val == 0

            left_removable = get_removable(node.left)
            right_removable = get_removable(node.right)
            if left_removable:
                node.left = None
            if right_removable:
                node.right = None

            if left_removable and right_removable and node.val == 0:
                return True
            else:
                return False

        if get_removable(root):
            return None

        return root


def test(testObj: unittest.TestCase, root_arr: List[int], expected: List[int]) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual_root = so.pruneTree(root)
    actual = treenode_to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, None, 0, 0, 1], [1, None, 0, None, 1])

    def test_2(self):
        test(self,   [1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1])

    def test_3(self):
        test(self,   [1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1])

    def test_4(self):
        test(self,   [], [])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 35 ms, faster than 88.94% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 13.9 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.
'''

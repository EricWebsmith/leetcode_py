from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from queue import Queue
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

null = None


class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node, parent_value=-1, depth=0):
            self.ans = max(self.ans, depth)
            if node is None:
                return

            if node.val == parent_value + 1:
                dfs(node.left, node.val, depth+1)
                dfs(node.right, node.val, depth+1)
            else:
                dfs(node.left, node.val, 1)
                dfs(node.right, node.val, 1)

        dfs(root, root.val, 1)

        return self.ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.longestConsecutive(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, null, 3, 2, 4, None, None, None, 5], 3)

    def test_2(self):
        test(self,   [2, None, 3, 2, None, 1], 2)

    def test_3(self):
        test(self,   [], 0)

    def test_4(self):
        test(self,   [2, None, 3, 2, 4, None, None, None, 5], 4)

    def test_5(self):
        test(self,   [1], 1)

    def test_6(self):
        test(self,   [1, 2, 3, 4, 5], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 120 ms, faster than 82.96% of Python3 online submissions for Binary Tree Longest Consecutive Sequence.
Memory Usage: 21.5 MB, less than 66.46% of Python3 online submissions for Binary Tree Longest Consecutive Sequence.
'''

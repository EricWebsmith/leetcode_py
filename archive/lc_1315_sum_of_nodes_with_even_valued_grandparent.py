
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def collect_grandchilren(self, node: TreeNode) -> None:
        if node.left:
            if node.left.left:
                self.ans += node.left.left.val
            if node.left.right:
                self.ans += node.left.right.val
        if node.right:
            if node.right.left:
                self.ans += node.right.left.val
            if node.right.right:
                self.ans += node.right.right.val

    def dfs(self, node: TreeNode) -> None:
        if node is None:
            return

        if node.val % 2 == 0:
            self.collect_grandchilren(node)

        self.dfs(node.left)
        self.dfs(node.right)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root)

        return self.ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.sumEvenGrandparent(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [6, 7, 8, 2, 7, 1, 3, 9,
             None, 1, 4, None, None, None, 5], 18)

    def test_2(self):
        test(self,   [1], 0)


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 141 ms, faster than 69.80% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 17.7 MB, less than 61.70% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
"""

import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def goodNodes(self, root: TreeNode) -> int:
        MIN_INT = - 1000000

        def dfs(node, max_value):
            if node is None:
                return

            if node.val >= max_value:
                self.ans += 1
                max_value = node.val
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, MIN_INT)
        return self.ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.goodNodes(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 1, 4, 3, None, 1, 5], 4)

    def test_2(self):
        test(self,   [3, 3, None, 4, 2], 3)

    def test_3(self):
        test(self,   [1], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 251 ms, faster than 96.75% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 33 MB, less than 7.60% of Python3 online submissions for Count Good Nodes in Binary Tree.
'''

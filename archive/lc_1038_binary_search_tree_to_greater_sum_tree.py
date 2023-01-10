import unittest
from typing import List

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def dfs(node, val) -> int:
            if node is None:
                return 0

            if node.right:
                node.val = node.val + dfs(node.right, val)
            else:
                node.val = node.val + val

            ans = node.val
            if node.left:
                ans = dfs(node.left, node.val)

            return ans

        dfs(root, 0)

        return root


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    assert root is not None
    actual_root = so.bstToGst(root)
    actual = treenode_to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8], [
             30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8])

    def test_2(self):
        test(self,   [0, None, 1], [1, None, 1])

    def test_3(self):
        test(self,   [1], [1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
31 ms
Beats
90.20%
'''

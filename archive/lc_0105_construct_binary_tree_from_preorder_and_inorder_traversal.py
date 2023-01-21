import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, treenode_to_array


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_val = preorder[0]
        root = TreeNode(preorder[0])
        left_length = inorder.index(root_val)
        root.left = self.buildTree(preorder[1 : left_length + 1], inorder[:left_length])
        root.right = self.buildTree(
            preorder[left_length + 1 :], inorder[left_length + 1 :]
        )
        return root


def test(
    testObj: unittest.TestCase,
    preorder: List[int],
    inorder: List[int],
    expected: Optional[TreeNode],
) -> None:
    so = Solution()
    actual_root = so.buildTree(preorder, inorder)
    actual = treenode_to_array(actual_root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7])

    def test_2(self):
        test(self, [-1], [-1], [-1])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
208 ms
Beats
65.62%
"""

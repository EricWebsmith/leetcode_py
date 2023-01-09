import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def get_leaves(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root]
        return self.get_leaves(root.left) + self.get_leaves(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_arr = self.get_leaves(root1)
        right_arr = self.get_leaves(root2)
        if len(left_arr) != len(right_arr):
            return False

        for left_node, right_node in zip(left_arr, right_arr):
            if left_node.val != right_node.val:
                return False

        return True


def test(testObj: unittest.TestCase, root1_arr: List[int], root2_arr: List[int], expected: bool) -> None:
    root1 = array_to_treenode(root1_arr)
    root2 = array_to_treenode(root2_arr)
    so = Solution()
    actual = so.leafSimilar(root1, root2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],  [
             3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8], True)

    def test_2(self):
        test(self,   [1, 2, 3],  [1, 3, 2], False)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
49 ms
Beats
73.77%
'''

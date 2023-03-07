import unittest
from typing import List, Optional

from leetcode_data_structure.binary_tree import TreeNode


class Solution:
    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None or node1.val != node2.val:
            return False

        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


def test(
    testObj: unittest.TestCase,
    root_arr: List[int | None],
    subRoot_arr: List[int | None],
    expected: bool,
) -> None:
    root = TreeNode.from_array(root_arr)
    subRoot = TreeNode.from_array(subRoot_arr)
    so = Solution()
    actual = so.isSubtree(root, subRoot)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 4, 5, 1, 2], [4, 1, 2], True)

    def test_2(self):
        test(self, [3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
243 ms
Beats
62.95%
"""

import unittest
from typing import List, Optional

from leetcode_data_structure.binary_tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def test(testObj: unittest.TestCase, root_arr: List[int|None], expected: Optional[TreeNode]) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()

    actual_root = so.invertTree(root)
    actual = TreeNode.to_array(actual_root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])

    def test_2(self):
        test(self, [2, 1, 3], [2, 3, 1])

    def test_3(self):
        test(self, [], [])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
26 ms
Beats
94.89%
"""

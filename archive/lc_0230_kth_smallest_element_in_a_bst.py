import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def __init__(self) -> None:
        self.visited = 0
        self.ans = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]):
            if self.visited >= k:
                return

            if node is None:
                return
            dfs(node.left)
            self.visited += 1
            if self.visited == k:
                self.ans = node.val
                return
            dfs(node.right)

        dfs(root)

        return self.ans


def test(
    testObj: unittest.TestCase, root_arr: List[int], k: int, expected: int
) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.kthSmallest(root, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 1, 4, None, 2], 1, 1)

    def test_2(self):
        test(self, [5, 3, 6, 2, 4, None, None, 1], 3, 3)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
47 ms
Beats
98.35%
"""

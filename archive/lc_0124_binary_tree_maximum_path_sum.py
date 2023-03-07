import unittest
from typing import List, Optional

from leetcode_data_structure import TreeNode


class Solution:
    def __init__(self) -> None:
        self.ans = -10000

    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.ans = max(self.ans, max(left, 0) + max(right, 0) + node.val)
        return max(left, right, 0) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans


def test(testObj: unittest.TestCase, root_arr: List[int|None], expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.maxPathSum(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3], 6)

    def test_2(self):
        test(self, [-10, 9, 20, None, None, 15, 7], 42)

    def test_3(self):
        test(self, [2, -1], 2)

    def test_4(self):
        test(self, [9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6], 16)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
126 ms
Beats
77.28%
"""

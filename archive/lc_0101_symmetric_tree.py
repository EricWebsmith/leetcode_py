import unittest
from typing import List, Optional

from leetcode_data_structure import TreeNode


def dfs(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False

    return dfs(a.left, b.right) and dfs(a.right, b.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return dfs(root.left, root.right)


def test(testObj: unittest.TestCase, root_arr: List[int | None], expected: bool) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.isSymmetric(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 2, 3, 4, 4, 3], True)

    def test_2(self):
        test(self, [1, 2, 2, None, 3, None, 3], False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
64 ms
Beats
55.17%
"""

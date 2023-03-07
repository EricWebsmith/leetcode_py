import unittest
from typing import List, Optional

from leetcode_data_structure import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def test(testObj: unittest.TestCase, root_arr: List[int|None], expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.maxDepth(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 9, 20, None, None, 15, 7], 3)

    def test_2(self):
        test(self, [1, None, 2], 2)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
47 ms
Beats
88.98%
"""

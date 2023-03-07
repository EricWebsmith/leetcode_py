import unittest
from typing import List, Optional

from leetcode_data_structure import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def pre(node):
            if not node:
                return 0
            return pre(node.left) + pre(node.right) + 1

        return pre(root)


def test(testObj: unittest.TestCase, root_arr: List[int|None], expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.countNodes(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5, 6], 6)

    def test_2(self):
        test(self, [], 0)

    def test_3(self):
        test(self, [1], 1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
158 ms
Beats
64.5%
"""

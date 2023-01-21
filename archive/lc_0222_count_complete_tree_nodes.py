import unittest
from typing import List

from data_structure.binary_tree import TreeNode, array_to_treenode


def get_left_depth(node: TreeNode | None) -> int:
    if node is None:
        return 0
    return get_left_depth(node.left) + 1


def get_right_depth(node: TreeNode | None) -> int:
    if node is None:
        return 0
    return get_right_depth(node.right) + 1


class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def dfs(node) -> int:
            if not node:
                return 0
            left_depth = get_left_depth(node)
            right_depth = get_right_depth(node)
            if left_depth == right_depth:
                return 2**left_depth - 1

            return dfs(node.left) + dfs(node.right) + 1

        return dfs(root)


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
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
77 ms
Beats
96.81%
"""

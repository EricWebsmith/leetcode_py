import unittest
from typing import List

from leetcode_data_structure import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]) -> TreeNode | None:
        nodes = set(nodes)  # type: ignore
        self.lca = None

        def dfs(node):
            if node is None:
                return False

            if node in nodes:
                self.lca = node
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                self.lca = node

            return left or right

        dfs(root)

        return self.lca


def test(
    testObj: unittest.TestCase,
    root_arr: List[int],
    nodes_arr: List[TreeNode],
    expected: int,
) -> None:
    root = TreeNode.from_array(root_arr)  # type: ignore
    nodes = TreeNode.get_by_vals(root, nodes_arr)  # type: ignore
    so = Solution()
    actual = so.lowestCommonAncestor(root, nodes)  # type: ignore
    testObj.assertEqual(actual.val, expected)  # type: ignore


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [4, 7], 2)

    def test_2(self):
        test(self, [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [1], 1)

    def test_3(self):
        test(self, [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [7, 6, 2, 4], 5)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 126 ms, faster than 95.83%
Memory Usage: 19.6 MB, less than 94.89%
"""

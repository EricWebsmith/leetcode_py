import unittest
from typing import List, Optional

from leetcode_data_structure import TreeNode


def get_sum(node: TreeNode | None):
    if node is None:
        return 0

    return node.val + get_sum(node.right) + get_sum(node.left)


class Solution:
    def __init__(self) -> None:
        self.maxProd = 0
        self.s = 0

    def dfs(self, node):
        if node is None:
            return 0
        subtree_sum = node.val + self.dfs(node.right) + self.dfs(node.left)
        product = (self.s - subtree_sum) * subtree_sum
        self.maxProd = max(self.maxProd, product)
        return subtree_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.s = get_sum(root)
        self.dfs(root)
        return self.maxProd % (10**9 + 7)


def test(testObj: unittest.TestCase, root_arr: List[int | None], expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()

    actual = so.maxProduct(root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5, 6], 110)

    def test_2(self):
        test(self, [1, None, 2, 3, 4, None, None, 5, 6], 90)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
378 ms
Beats
85.85%
"""

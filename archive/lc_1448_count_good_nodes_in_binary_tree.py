import unittest
from typing import List

from leetcode_data_structure import TreeNode


class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def goodNodes(self, root: TreeNode) -> int:
        MIN_INT = -1000000

        def dfs(node, max_value):
            if node is None:
                return

            if node.val >= max_value:
                self.ans += 1
                max_value = node.val
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, MIN_INT)
        return self.ans


def test(testObj: unittest.TestCase, root_arr: List[int | None], expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.goodNodes(root)  # type: ignore
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 1, 4, 3, None, 1, 5], 4)

    def test_2(self):
        test(self, [3, 3, None, 4, 2], 3)

    def test_3(self):
        test(self, [1], 1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 251 ms, faster than 96.75%
Memory Usage: 33 MB, less than 7.60%
"""

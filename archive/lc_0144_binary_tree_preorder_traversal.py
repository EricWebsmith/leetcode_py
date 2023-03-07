import unittest

from leetcode_data_structure.binary_tree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


def test(testObj: unittest.TestCase, root_arr: list[int|None], expected: list[int]) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.preorderTraversal(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, None, 2, 3], [1, 2, 3])

    def test_2(self):
        test(self, [], [])

    def test_3(self):
        test(self, [1], [1])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
35 ms
Beats
74.39%
"""

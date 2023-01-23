import unittest

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


def test(testObj: unittest.TestCase, root_arr: list[int], expected: list[int]) -> None:
    root = array_to_treenode(root_arr)
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

import unittest

from leetcode_data_structure import TreeNode


class Solution:
    def removeLeafNodes(self, root: TreeNode | None , target: int) -> TreeNode | None:
        pre_root = TreeNode(target + 1)
        pre_root.left = root

        def dfs(node: TreeNode) -> bool:
            if node is None:
                return True

            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None

            if node.left is None and node.right is None and node.val == target:
                return True

            return False

        dfs(pre_root)

        return pre_root.left


def test(
    testObj: unittest.TestCase,
    root_arr: list[int | None],
    target: int,
    expected: list[int | None],
) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()

    actual_root = so.removeLeafNodes(root, target)
    actual = TreeNode.to_array(actual_root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 2, None, 2, 4], 2, [1, None, 3, None, 4])

    def test_2(self):
        test(self, [1, 3, 3, 3, 2], 3, [1, 3, None, None, 2])

    def test_3(self):
        test(self, [1, 2, None, 2, None, 2], 2, [1])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 54 ms, faster than 92.66%
Memory Usage: 14.7 MB, less than 50.52%
"""

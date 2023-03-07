import unittest

from leetcode_data_structure import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        stack: list[tuple[TreeNode | None, int]] = [(root, 1)]
        ans = 0
        while stack:
            node, depth = stack.pop()
            if node is not None:
                ans = max(ans, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return ans


def test(testObj: unittest.TestCase, root_arr: list[int|None], expected: int) -> None:
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
40 ms
Beats
96.91%
"""

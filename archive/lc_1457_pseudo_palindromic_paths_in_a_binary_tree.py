import unittest
from typing import Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        value_counts = [0] * 10

        def is_palindrome(counts):
            return sum(counts) <= 1

        def traceback(node: TreeNode):
            if node.left is None and node.right is None:
                if is_palindrome(value_counts):
                    self.ans += 1
                return

            if node.left:
                value_counts[node.left.val] ^= 1
                traceback(node.left)
                value_counts[node.left.val] ^= 1

            if node.right:
                value_counts[node.right.val] ^= 1
                traceback(node.right)
                value_counts[node.right.val] ^= 1

        value_counts[root.val] ^= 1
        traceback(root)

        return self.ans


def test(testObj: unittest.TestCase, root_arr: list[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.pseudoPalindromicPaths(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [2, 3, 1, 3, 1, None, 1], 2)

    def test_2(self):
        test(self,   [2, 1, 1, 1, 3, None, None, None, None, None, 1], 1)

    def test_3(self):
        test(self,   [9], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 885 ms, faster than 94.08%
Memory Usage: 85.3 MB, less than 65.11%
'''

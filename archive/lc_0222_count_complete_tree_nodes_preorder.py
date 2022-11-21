import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def pre(node):
            if not node:
                return 0
            return pre(node.left) + pre(node.right) + 1

        return pre(root)


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.countNodes(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 4, 5, 6], 6)

    def test_2(self):
        test(self,   [], 0)

    def test_3(self):
        test(self,   [1], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
158 ms
Beats
64.5%
'''

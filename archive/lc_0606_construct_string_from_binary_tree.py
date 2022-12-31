import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        ans = f'{root.val}'
        if root.left and root.right:
            ans += f'({self.tree2str(root.left)})({self.tree2str(root.right)})'
        elif not root.left and root.right:
            ans += f'()({self.tree2str(root.right)})'
        elif root.left and not root.right:
            ans += f'({self.tree2str(root.left)})'

        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: str) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()

    actual = so.tree2str(root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 4], "1(2(4))(3)")

    def test_2(self):
        test(self,   [1, 2, 3, None, 4], "1(2()(4))(3)")


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 49 ms, faster than 96.44%
Memory Usage: 16.3 MB, less than 95.12%
'''

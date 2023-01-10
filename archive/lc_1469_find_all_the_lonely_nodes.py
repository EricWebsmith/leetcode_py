import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans: list = []
        if root is None:
            return []

        def dfs(node):
            if node.left is not None and node.right is None:
                ans.append(node.left.val)
                dfs(node.left)
            elif node.left is None and node.right is not None:
                ans.append(node.right.val)
                dfs(node.right)
            elif node.left is not None and node.right is not None:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.getLonelyNodes(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, None, 4], [4])

    def test_2(self):
        test(self,   [7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], [6, 2])

    def test_3(self):
        test(self,   [11, 99, 88, 77, None, None, 66, 55, None, None, 44, 33, None, None, 22], [77, 55, 33, 66, 44, 22])

    def test_4(self):
        test(self,   [], [])

    def test_5(self):
        test(self,   [1, 2, 3], [])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 60 ms, faster than 87.98%
Memory Usage: 15.2 MB, less than 44.29%
'''

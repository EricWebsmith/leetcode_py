import unittest
from typing import Optional

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)

null = None


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        current_depth = 1
        q: list = [root]
        while q:
            new_q: list = []
            for node in q:
                assert node is not None
                if current_depth == depth - 1:
                    left = node.left
                    node.left = TreeNode(val)
                    node.left.left = left
                    right = node.right
                    node.right = TreeNode(val)
                    node.right.right = right
                else:
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
            q = new_q
            current_depth += 1

        return root


def test(testObj: unittest.TestCase, root_arr: list[int], val: int, depth: int, expected: Optional[TreeNode]) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()

    actual_root = so.addOneRow(root, val, depth)
    actual = treenode_to_array(actual_root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [4, 2, 6, 3, 1, 5],  1,  2, [
             4, 1, 1, 2, None, None, 6, 3, 1, 5])

    def test_2(self):
        test(self,   [4, 2, None, 3, 1],  1,  3, [
             4, 2, None, 1, 1, 3, None, None, 1])

    def test_3(self):
        test(self,   [4, 2, 6, 3, 1, 5],  1,  3, [
             4, 2, 6, 1, 1, 1, 1, 3, null, null, 1, 5])

    def test_4(self):
        test(self,   [4, 2, 6, 3, 1, 5],  1,  1, [1, 4, null, 2, 6, 3, 1, 5])


if __name__ == '__main__':
    unittest.main()

'''
74ms, 72%
'''

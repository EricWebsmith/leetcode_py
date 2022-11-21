import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test(testObj: unittest.TestCase, p_arr: List[int], q_arr: List[int], expected: bool) -> None:
    p = array_to_treenode(p_arr)
    q = array_to_treenode(q_arr)
    so = Solution()

    actual = so.isSameTree(p, q)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3],  [1, 2, 3], True)

    def test_2(self):
        test(self,   [1, 2],  [1, None, 2], False)

    def test_3(self):
        test(self,   [1, 2, 1],  [1, 1, 2], False)


if __name__ == '__main__':
    unittest.main()

'''

'''

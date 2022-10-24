import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        check = None
        stack = []
        for n in preorder:
            while stack and n > stack[-1]:
                check = stack.pop()
            if check != None and n < check:
                return False
            stack.append(n)
        return True


def test(testObj: unittest.TestCase, preorder: List[int], expected: int) -> None:

    so = Solution()
    actual = so.verifyPreorder(preorder)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [5, 2, 1, 3, 6], True)

    def test_2(self):
        test(self,   [5, 2, 6, 1, 3], False)

    def test_3(self):
        test(self,   [3, 1, 2], True)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 239 ms, faster than 88.43% of Python3 online submissions for Verify Preorder Sequence in Binary Search Tree.
Memory Usage: 14.9 MB, less than 66.44% of Python3 online submissions for Verify Preorder Sequence in Binary Search Tree.
'''

import unittest
from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode

null = None


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        ans: list[list[int]] = []
        q = deque([root])
        qsize = len(q)
        while qsize > 0:
            layer: list = []
            for _ in range(qsize):
                node = q.popleft()
                layer.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(layer)
            qsize = len(q)
        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: List[List[int]]) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.levelOrder(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])

    def test_2(self):
        test(self,   [1], [[1]])

    def test_3(self):
        test(self,   [], [])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
56 ms
Beats
73.4%
'''

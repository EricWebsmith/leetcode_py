import unittest
from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        qsize = len(q)
        levels = 0
        while qsize > 0:
            levels += 1
            for _ in range(qsize):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            qsize = len(q)

        return levels


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.maxDepth(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 9, 20, None, None, 15, 7], 3)

    def test_2(self):
        test(self, [1, None, 2], 2)

    def test_3(self):
        test(self, [], 0)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
53 ms
Beats
81.47%
"""

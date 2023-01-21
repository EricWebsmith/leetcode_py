import unittest
from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode

null = None


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        q_size = len(q)
        while q_size > 0:

            for i in range(q_size):
                node = q.popleft()

                if node.val == u.val:
                    if i < q_size - 1:
                        return q.popleft()
                    else:
                        return None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            q_size = len(q)

        return None


def test(
    testObj: unittest.TestCase, root_arr: List[int], u_arr: List[int], expected: int
) -> None:
    root = array_to_treenode(root_arr)
    u = array_to_treenode([u_arr])
    so = Solution()
    actual = so.findNearestRightNode(root, u)
    if actual:
        testObj.assertEqual(actual.val, expected)
    else:
        testObj.assertTrue(expected is None)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, None, 4, 5, 6], 4, 5)

    def test_2(self):
        test(self, [3, None, 4, 2], 2, None)

    def test_3(self):
        test(self, [2], 2, None)

    def test_4(self):
        test(self, [1, 2, 3], 2, 3)

    def test_5(self):
        test(self, [1, 2, 3], 3, None)

    def test_6(self):
        test(
            self,
            [
                3,
                10,
                1,
                7,
                8,
                9,
                4,
                null,
                null,
                2,
                null,
                null,
                11,
                null,
                null,
                null,
                null,
                5,
                null,
                6,
            ],
            4,
            None,
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 347 ms, faster than 91.98%
Memory Usage: 51.8 MB, less than 74.26%
"""

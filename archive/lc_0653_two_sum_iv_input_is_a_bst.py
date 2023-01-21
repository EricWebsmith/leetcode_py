import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


def inorder(node) -> List[int]:
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = inorder(root)
        n = len(arr)
        left = 0
        right = n - 1
        while left < right:
            s = arr[left] + arr[right]
            if s == k:
                return True
            elif s > k:
                right -= 1
            else:
                left += 1

        return False


def test(
    testObj: unittest.TestCase, root_arr: List[int], k: int, expected: bool
) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.findTarget(root, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [5, 3, 6, 2, 4, None, 7], 9, True)

    def test_2(self):
        test(self, [5, 3, 6, 2, 4, None, 7], 28, False)

    def test_3(self):
        test(self, [2, 1, 3], 3, True)


if __name__ == "__main__":
    unittest.main()

"""
124ms, 72.43%
"""

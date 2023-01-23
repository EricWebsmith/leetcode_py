import unittest
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

    def __repr__(self) -> str:
        return str(self.val)


def array_to_treenode(arr: list[int]) -> TreeNode | None:
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    for i in range(1, len(arr), 2):
        node = q.popleft()
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        if i + 1 < len(arr) and arr[i + 1] is not None:
            node.right = TreeNode(arr[i + 1])
            q.append(node.right)

    return root


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test(testObj: unittest.TestCase, p_arr: list[int], q_arr: list[int], expected: bool) -> None:
    p = array_to_treenode(p_arr)
    q = array_to_treenode(q_arr)
    so = Solution()
    actual = so.isSameTree(p, q)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3], [1, 2, 3], True)

    def test_2(self):
        test(self, [1, 2], [1, None, 2], False)

    def test_3(self):
        test(self, [1, 2, 1], [1, 1, 2], False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
28 ms
Beats
93.78%
"""

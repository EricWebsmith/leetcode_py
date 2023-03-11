import unittest
from leetcode_data_structure import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test(testObj: unittest.TestCase, p_arr: list[int | None], q_arr: list[int | None], expected: bool) -> None:
    p = TreeNode.from_array(p_arr)
    q = TreeNode.from_array(q_arr)
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

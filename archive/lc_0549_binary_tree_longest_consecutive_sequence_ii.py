import unittest
from typing import List, Optional

from leetcode_data_structure.binary_tree import TreeNode


class Solution:
    def __init__(self) -> None:
        self.path = 0

    def dfs(self, node):
        if node is None:
            return 0, 0

        left_increase, left_decrease = self.dfs(node.left)
        right_increase, right_decrease = self.dfs(node.right)

        # increase
        depth_increase = 1
        if left_increase > 0 and (node.val - node.left.val) == -1:
            depth_increase = left_increase + 1
        if right_increase > 0 and (node.val - node.right.val) == -1:
            depth_increase = max(depth_increase, right_increase + 1)

        # decrease
        depth_decrease = 1
        if left_decrease > 0 and (node.val - node.left.val) == 1:
            depth_decrease = left_decrease + 1
        if right_decrease > 0 and (node.val - node.right.val) == 1:
            depth_decrease = max(depth_decrease, right_decrease + 1)

        # increase from left (decrease) to right (increase)
        path_left_to_right = 1
        if left_decrease > 0 and (node.val - node.left.val) == 1:
            path_left_to_right += left_decrease
        if right_increase > 0 and (node.val - node.right.val) == -1:
            path_left_to_right += right_increase

        self.path = max(self.path, path_left_to_right)

        # increase from right (decrease) to left (increase)
        path_right_to_left = 1
        if right_decrease > 0 and (node.val - node.right.val) == 1:
            path_right_to_left += right_decrease
        if left_increase > 0 and (node.val - node.left.val) == -1:
            path_right_to_left += left_increase

        self.path = max(self.path, path_right_to_left)

        return depth_increase, depth_decrease

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.path


def test(testObj: unittest.TestCase, root_arr: List[int | None], expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.longestConsecutive(root)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3], 2)

    def test_2(self):
        test(self, [2, 1, 3], 3)

    def test_3(self):
        test(self, [], 0)

    def test_4(self):
        test(self, [1, 2, 3, 4, 2], 2)

    def test_5(self):
        test(
            self,
            [
                4,
                -7,
                -3,
                None,
                None,
                -9,
                -3,
                9,
                -7,
                -4,
                None,
                6,
                None,
                -6,
                -6,
                None,
                None,
                0,
                6,
                5,
                None,
                9,
                None,
                None,
                -1,
                -4,
                None,
                None,
                None,
                -2,
            ],
            2,
        )

    def test_6(self):
        test(self, [2, None, 3, 4, None, 1], 3)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 70 ms, faster than 71.13%
Memory Usage: 16.4 MB, less than 45.27%
"""

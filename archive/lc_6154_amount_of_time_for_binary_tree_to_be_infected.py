import unittest
from typing import List, Optional

from leetcode_data_structure.binary_tree import TreeNode, array_to_treenode

DOWN = 1
UP = -1


class Solution:
    def __init__(self) -> None:
        self.distance = 0
        self.start = 0
        self.path: list = []

    def backtrack(self, current):
        last_node = current[-1]
        if last_node is None:
            return False

        if last_node.val == self.start:
            self.path = current.copy()
            return True

        current.append(last_node.left)
        if self.backtrack(current):
            return True
        current.pop()

        current.append(last_node.right)
        if self.backtrack(current):
            return True
        current.pop()

    def get_depth(self, node, depth=0):
        if node is None:
            return max(depth - 1, 0)

        return max(self.get_depth(node.left, depth + 1), self.get_depth(node.right, depth + 1))

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.start = start

        temp_path = [root]
        self.backtrack(temp_path)
        path = self.path

        path_len = len(path)

        target_depth = self.get_depth(path[-1])
        ans = max(target_depth, 0)

        for i in range(path_len - 1):
            start_node = None
            if path[i].left == path[i + 1]:
                start_node = path[i].right
            else:
                start_node = path[i].left
            down = 0
            if start_node:
                down = self.get_depth(start_node) + 1
            ans = max(ans, down + (path_len - i - 1))

        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], start: int, expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.amountOfTime(root, start)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [1, 5, 3, None, 4, 10, 6, 9, 2], 3, 4)

    def test_2(self):
        test(self, [1], 1, 0)

    def test_3(self):
        test(self, [1, 2, None, 3, None, 4, None, 5], 1, 4)

    def test_4(self):
        test(self, [1, 2, None, 3, None, 4, None, 5], 3, 2)


if __name__ == "__main__":
    unittest.main()

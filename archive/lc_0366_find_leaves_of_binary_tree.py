import unittest
from typing import List, Optional

from data_structure.binary_tree import TreeNode, array_to_treenode


class Solution:
    def __init__(self) -> None:
        self.dict: dict = dict()

    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        level = max(left, right) + 1
        if level not in self.dict:
            self.dict[level] = []
        self.dict[level].append(node.val)
        return level

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.dfs(root)
        keys = [k for k in self.dict.keys()]
        keys.sort()
        ans: list = []
        for key in keys:
            ans.append(self.dict[key])

        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: List[List[int]]) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()

    actual = so.findLeaves(root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5], [[4, 5, 3], [2], [1]])

    def test_2(self):
        test(self, [1], [[1]])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 29 ms, faster than 97.10%
Memory Usage: 13.8 MB, less than 74.47%
"""

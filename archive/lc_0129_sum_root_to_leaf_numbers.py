import unittest

from leetcode_data_structure import TreeNode


class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def dfs(self, node: TreeNode | None, val: int):
        if node is None:
            return
        
        new_val = val * 10 + node.val
        if node.left is None and node.right is None:
            self.ans += new_val
        
        self.dfs(node.left, new_val)
        self.dfs(node.right, new_val)


    def sumNumbers(self, root: TreeNode | None) -> int:
        self.dfs(root, 0)
        return self.ans


def test(testObj: unittest.TestCase, root_arr: list[int | None], expected: int) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.sumNumbers(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,2,3], 25)

    def test_2(self):
        test(self,   [4,9,0,5,1], 1026)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
24 ms
Beats
97.50%
'''

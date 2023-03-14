import unittest
from collections import deque
from leetcode_data_structure import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        
        ans = []
        q = deque([root])
        q_len = len(q)
        while(q_len>0):
            current = []
            for _ in range(q_len):
                node = q.popleft()
                current.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(current)
            q_len = len(q)
        ans.reverse()
        return ans


def test(testObj: unittest.TestCase, root_arr: list[int | None], expected: list[list[int]]) -> None:
    root = TreeNode.from_array(root_arr)
    so = Solution()
    actual = so.levelOrderBottom(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [3,9,20,None,None,15,7], [[15,7],[9,20],[3]])

    def test_2(self):
        test(self,   [1], [[1]])

    def test_3(self):
        test(self,   [], [])


if __name__ == '__main__':
    unittest.main()


'''
Runtime
35 ms
Beats
73.54%
'''

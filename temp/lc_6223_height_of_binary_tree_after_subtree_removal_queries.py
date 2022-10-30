import unittest
from typing import Dict, List, Optional

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)

null = None


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        d = {}
        d_height: Dict[int, int] = {}
        d_p: Dict[int, int] = {}

        def dfs(node):
            if node == None:
                return -1
            d[node.val] = node
            if node.left:
                d_p[node.left.val] = node.val
            if node.right:
                d_p[node.right.val] = node.val
            h = max(dfs(node.left), dfs(node.right)) + 1
            d_height[node.val] = h
            return h

        dfs(root)

        ans = []
        for q in queries:
            h = -1
            c = q
            p = d_p[c]
            while True:
                p_node = d[p]
                other = None
                if p_node.left and p_node.left.val == c:
                    other = p_node.right
                if p_node.right and p_node.right.val == c:
                    other = p_node.left

                if other:
                    h = max(h, d_height[other.val]) + 1
                else:
                    h = h + 1

                if p == root.val:
                    break

                if h == d_height[p]:
                    h = d_height[root.val]
                    break

                c = p
                p = d_p[c]
            ans.append(h)

        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], queries: List[int], expected: List[int]) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.treeQueries(root, queries)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3, 4, 2, None, 6, 5, None,
             None, None, None, None, 7],  [4], [2])

    def test_2(self):
        test(self,   [5, 8, 9, 2, 1, 3, 7, 4, 6],  [3, 2, 4, 8], [3, 2, 3, 2])

    def test_3(self):
        test(self,   [1, 2],  [2], [0])

    def test_4(self):
        test(self,   [1, null, 5, 3, null, 2, 4],
             [3, 5, 4, 2, 4],  [1, 0, 3, 3, 3])


if __name__ == '__main__':
    unittest.main()

'''

'''

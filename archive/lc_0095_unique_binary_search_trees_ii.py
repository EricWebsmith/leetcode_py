import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(start, end):
            n = end - start + 1
            if n <= 0:
                return [None]
            if n == 1:
                return [TreeNode(start)]

            ans = []
            for i in range(start, end+1):
                lefts = dfs(start, i-1)
                rights = dfs(i+1, end)
                for left in lefts:
                    for right in rights:
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        ans.append(node)
            return ans

        return dfs(1, n)


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()
    trees = so.generateTrees(n)
    actual = [treenode_to_array(t) for t in trees]
    actual.sort()
    expected.sort()
    # print(actual)
    # print(expected)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   3, [[1, None, 2, None, 3], [1, None, 3, 2], [
             2, 1, 3], [3, 1, None, None, 2], [3, 2, None, 1]])

    def test_2(self):
        test(self,   1, [[1]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 53 ms, faster than 98.29% of Python3 online submissions for Unique Binary Search Trees II.
Memory Usage: 15.7 MB, less than 76.03% of Python3 online submissions for Unique Binary Search Trees II.
'''

from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt

from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])

        q_size = 1
        ans = []
        while q_size > 0:
            layer_sum = 0

            for i in range(q_size):
                node = q.popleft()
                layer_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(layer_sum/q_size)
            q_size = len(q)

        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_treenode(root_arr)
    so = Solution()
    actual = so.averageOfLevels(root)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 9, 20, None, None, 15, 7],
             [3.00000, 14.50000, 11.00000])

    def test_2(self):
        test(self,   [3, 9, 20, 15, 7], [3.00000, 14.50000, 11.00000])

    def test_3(self):
        test(self,   [1], [1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 47 ms, faster than 98.17% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.5 MB, less than 87.46% of Python3 online submissions for Average of Levels in Binary Tree.
'''

from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def __init__(self) -> None:
        self.max_diameter = 0

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def dfs(node: Node) -> int:
            second_max_radius = 0
            max_radius = 0
            if node.children is None or len(node.children) == 0:
                return 1

            for child in node.children:
                current_radius = dfs(child)
                if current_radius > max_radius:
                    second_max_radius = max_radius
                    max_radius = current_radius
                elif current_radius > second_max_radius:
                    second_max_radius = current_radius

            current_diameter = max_radius + second_max_radius
            self.max_diameter = max(self.max_diameter, current_diameter)
            return max_radius + 1

        dfs(root)

        return self.max_diameter


def test(testObj: unittest.TestCase, root_arr: List[int], expected: int) -> None:
    root = array_to_node(root_arr)
    so = Solution()

    actual = so.diameter(root)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, None, 3, 2, 4, None, 5, 6], 3)

    def test_2(self):
        test(self,   [1, None, 2, None, 3, 4, None, 5, None, 6], 4)

    def test_3(self):
        test(self,   [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None,
             9, 10, None, None, 11, None, 12, None, 13, None, None, 14], 7)

    def test_4(self):
        test(self,   [1, None, 2, 3], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 57 ms, faster than 81.99% of Python3 online submissions for Diameter of N-Ary Tree.
Memory Usage: 16 MB, less than 53.92% of Python3 online submissions for Diameter of N-Ary Tree.
'''
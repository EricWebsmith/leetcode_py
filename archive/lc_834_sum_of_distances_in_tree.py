from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        count = [1] * n
        ans = [0] * n

        def dfs(node: int = 0, parent: Optional[int] = None):
            for child in g[node]:
                if child == parent:
                    continue
                dfs(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

        def dfs2(node: int = 0, parent: Optional[int] = None):
            for child in g[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + n - count[child]
                dfs2(child, node)

        dfs()
        dfs2()

        return ans


def test(testObj: unittest.TestCase, n: int, edges: List[List[int]], expected: List[int]) -> None:

    so = Solution()

    actual = so.sumOfDistancesInTree(n, edges)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   6,  [[0, 1], [0, 2], [2, 3], [
             2, 4], [2, 5]], [8, 12, 6, 10, 10, 10])

    def test_2(self):
        test(self,   1,  [], [0])

    def test_3(self):
        test(self,   2,  [[1, 0]], [1, 1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1112 ms, faster than 90.00% of Python3 online submissions for Sum of Distances in Tree.
Memory Usage: 65.9 MB, less than 38.81% of Python3 online submissions for Sum of Distances in Tree.
'''

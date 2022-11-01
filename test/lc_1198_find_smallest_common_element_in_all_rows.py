import unittest
from collections import defaultdict, deque
from functools import cache
from heapq import heappop, heappush
from math import sqrt
from typing import Any, Dict, List, Optional, Set

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)
from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)
from data_structure.nary_tree import Node, array_to_node, node_to_array

null = None


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cur_max = mat[0][0]
        cnt = 0
        p = [0] * m
        while True:

            for r in range(m):
                while p[r] < m and mat[r][p[r]] < cur_max:
                    p[r] += 1

                if p[r] == n:
                    return -1

                if cur_max == mat[r][p[r]]:
                    cnt += 1
                else:
                    cur_max = mat[r][p[r]]
                    cnt = 1

                if cnt == m:
                    return cur_max

        return -1


def test(testObj: unittest.TestCase, mat: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.smallestCommonElement(mat)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10],
             [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]], 5)

    def test_2(self):
        test(self,   [[1, 2, 3], [2, 3, 4], [2, 3, 5]], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
530 ms
Beats
88.92%
'''

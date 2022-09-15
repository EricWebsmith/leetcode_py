from functools import cache
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()

        @cache
        def dp(i, j, k):
            if k == 1:
                total_distance = 0
                while i < j:
                    total_distance += houses[j] - houses[i]
                    i += 1
                    j -= 1
                return total_distance

            return min(dp(i, m, k-1) + dp(m+1, j, 1) for m in range(i+k-2, j))

        return dp(0, n-1, k)


def test(testObj: unittest.TestCase, houses: List[int], k: int, expected: int) -> None:
    so = Solution()
    actual = so.minDistance(houses, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 4, 8, 10, 20],  3, 5)

    def test_2(self):
        test(self,   [2, 3, 5, 12, 18],  2, 9)

    def test_3(self):
        test(self,   [3, 6, 14, 10], 4,  0)

    def test_4(self):
        test(self,  [1, 3, 13, 7, 6], 2, 9)

    def test_5(self):
        test(self,  [2, 5, 7, 10, 14], 2, 9)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 293 ms, faster than 96.34% of Python3 online submissions for Allocate Mailboxes.
Memory Usage: 16.3 MB, less than 39.94% of Python3 online submissions for Allocate Mailboxes.
'''

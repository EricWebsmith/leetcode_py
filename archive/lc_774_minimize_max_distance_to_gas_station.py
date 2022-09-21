from heapq import heapify, heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= k

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo


def test(testObj: unittest.TestCase, stations: List[int], k: int, expected: float) -> None:

    so = Solution()

    actual = so.minmaxGasDist(stations, k)
    print(actual, expected)
    testObj.assertAlmostEqual(actual, expected, 5)
    # testObj.assertTrue(abs(actual-expected) < 0.000001)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  9, 0.50000)

    def test_2(self):
        test(self,   [23, 24, 36, 39, 46, 56, 57, 65, 84, 98],  1, 14.00000)

    def test_3(self):
        test(self,   [10, 19, 25, 27, 56, 63, 70, 87, 96, 97], 3, 9.66667)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 668 ms, faster than 48.34% of Python3 online submissions for Minimize Max Distance to Gas Station.
Memory Usage: 14.2 MB, less than 79.38% of Python3 online submissions for Minimize Max Distance to Gas Station.
'''

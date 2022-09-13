from bisect import bisect_right
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = [nums1[i]-nums2[i] for i in range(n)]
        diff.sort()

        ans = 0
        index = 0
        pair = n
        while index < n and diff[index] <= 0:
            target = -diff[index]
            pair = bisect_right(diff, target, lo=index, hi=pair)
            ans += n - pair
            index += 1

        n_positive = n - index
        if n_positive >= 2:
            ans += n_positive * (n_positive-1) // 2

        return ans


def test(testObj: unittest.TestCase, nums1: List[int], nums2: List[int], expected: int) -> None:

    so = Solution()
    actual = so.countPairs(nums1, nums2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [2, 1, 2, 1],  [1, 2, 1, 2], 1)

    def test_2(self):
        test(self,   [1, 10, 6, 2],  [1, 4, 1, 5], 5)

    def test_3(self):
        test(self,   [1],  [1], 0)

    def test_4(self):
        test(self,   [1, 1],  [1, 1], 0)

    def test_5(self):
        test(self,   [1, 2],  [1, 1], 1)

    def test_6(self):
        test(self,   [1, 5],  [2, 3], 1)

    def test_7(self):
        test(self,   [1, 4],  [2, 3], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1102 ms, faster than 95.89% of Python3 online submissions for Count Pairs in Two Arrays.
Memory Usage: 32.5 MB, less than 40.18% of Python3 online submissions for Count Pairs in Two Arrays.
'''

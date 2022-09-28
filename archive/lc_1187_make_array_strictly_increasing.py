
from bisect import bisect_right
import unittest
from functools import cache
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        MAX_INT = 10000
        m = len(arr1)
        n = len(arr2)
        arr2.sort()

        @cache
        def dfs(i, moving_max):
            if i == m:
                return 0

            a = MAX_INT
            # operate
            candidate_index = bisect_right(arr2, moving_max)
            if candidate_index < n:
                a = dfs(i+1, arr2[candidate_index])+1

            # no operate
            # only when increasing, can we skip operation.
            b = MAX_INT
            if arr1[i] > moving_max:
                b = dfs(i+1, arr1[i])

            return min(a, b)

        ans = dfs(0, -1)

        return -1 if ans == MAX_INT else ans


def test(testObj: unittest.TestCase, arr1: List[int], arr2: List[int], expected: int) -> None:

    so = Solution()

    actual = so.makeArrayIncreasing(arr1, arr2)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 5, 3, 6, 7],  [1, 3, 2, 4], 1)

    def test_2(self):
        test(self,   [1, 5, 3, 6, 7],  [4, 3, 1], 2)

    def test_3(self):
        test(self,   [1, 5, 3, 6, 7],  [1, 6, 3, 3], -1)

    def test_4(self):
        test(self,   [0, 11, 6, 1, 4, 3], [5, 4, 11, 10, 1, 0], 5)

    def test_5(self):
        test(self,   [1, 2, 3, 2, 1], [4, 5], 2)

    def test_6(self):
        test(self,   [1, 2, 1, 2, 1], [3, 4, 5], 3)

    def test_7(self):
        test(self,   [31, 18, 1, 12, 23, 14, 25, 4, 17, 18, 29, 28, 35, 34, 19, 8, 25, 6, 35],
             [13, 10, 25, 18, 3, 8, 37, 20, 23, 12, 9, 36, 17, 22, 29, 6, 1, 12, 37, 6, 3, 14, 37, 2], 19)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 797 ms, faster than 87.79% of Python3 online submissions for Make Array Strictly Increasing.
Memory Usage: 136.4 MB, less than 48.85% of Python3 online submissions for Make Array Strictly Increasing.
'''

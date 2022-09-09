from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def get_missing(nums: List[int], mid: int) -> int:
            return nums[mid] - nums[0] - mid

        left = 0
        right = n - 1
        while left < right:
            mid = (left + right + 1) >> 1
            missing = get_missing(nums, mid)
            if missing < k:
                left = mid
            else:
                right = mid - 1

        missing = get_missing(nums, left)

        return nums[left] + (k - missing)


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: int) -> None:

    so = Solution()

    actual = so.missingElement(nums, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [4, 7, 9, 10],  1, 5)

    def test_2(self):
        test(self,   [4, 7, 9, 10],  3, 8)

    def test_3(self):
        test(self,   [1, 2, 4],  3, 6)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 295 ms, faster than 95.76% of Python3 online submissions for Missing Element in Sorted Array.
Memory Usage: 20.4 MB, less than 37.68% of Python3 online submissions for Missing Element in Sorted Array.
'''

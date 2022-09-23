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
    def firstMissingPositive(self, nums: List[int]) -> int:
        has_one = False
        for num in nums:
            if num == 1:
                has_one = True
                break

        if not has_one:
            return 1

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 1
            if nums[i] > n:
                nums[i] = 1

        for i in range(n):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])

        for i in range(1, n):
            if nums[i] > 0:
                return i+1

        return n+1


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()

    actual = so.firstMissingPositive(nums)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 0], 3)

    def test_2(self):
        test(self,   [3, 4, -1, 1], 2)

    def test_3(self):
        test(self,   [7, 8, 9, 11, 12], 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 317 ms, faster than 86.74% of Python3 online submissions for First Missing Positive.
Memory Usage: 27.3 MB, less than 63.57% of Python3 online submissions for First Missing Positive.
'''

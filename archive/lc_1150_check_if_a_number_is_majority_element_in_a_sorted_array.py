from bisect import bisect_left, bisect_right
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n % 2 == 0:
            left = nums[n//2-1]
            right = nums[n//2]
            if left != right:
                return False

        candidate = nums[n//2]
        if candidate != target:
            return False
        c = bisect_right(nums, candidate) - bisect_left(nums, candidate)
        return c > n//2


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected: int) -> None:

    so = Solution()
    actual = so.isMajorityElement(nums, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [2, 4, 5, 5, 5, 5, 5, 6, 6],  5, True)

    def test_2(self):
        test(self,   [10, 100, 101, 101],  101, False)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 40 ms, faster than 92.86% of Python3 online submissions for Check If a Number Is Majority Element in a Sorted Array.
Memory Usage: 14 MB, less than 82.74% of Python3 online submissions for Check If a Number Is Majority Element in a Sorted Array.
'''


from heapq import heappop, heappush
import unittest
from typing import List, Optional
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return list(filter(lambda x: x < pivot, nums)) + list(filter(lambda x: x == pivot, nums)) + list(filter(lambda x: x > pivot, nums))


def test(testObj: unittest.TestCase, nums: List[int], pivot: int, expected: int) -> None:

    so = Solution()
    actual = so.pivotArray(nums, pivot)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14])

    def test_2(self):
        test(self,   [-3, 4, 3, 2], 2, [-3, 2, 4, 3])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1754 ms, faster than 78.80% of Python3 online submissions for Partition Array According to Given Pivot.
Memory Usage: 31.6 MB, less than 42.17% of Python3 online submissions for Partition Array According to Given Pivot.
'''

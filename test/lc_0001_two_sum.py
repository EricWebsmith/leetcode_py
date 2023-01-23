from heapq import heappop, heappush
import unittest
from functools import cache
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
from data_structure.link_list import ListNode, listnode_to_array, array_to_listnode


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        

        pass


def test(testObj: unittest.TestCase, nums: list[int], expected:list[int]) -> None:
    so = Solution()
    actual = so.twoSum(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [2,7,11,15],  9, [0,1])

    def test_2(self):
        test(self,   [3,2,4],  6, [1,2])

    def test_3(self):
        test(self,   [3,3],  6, [0,1])


if __name__ == '__main__':
    unittest.main()


'''

'''

from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count_missing = lambda m: nums[m] - nums[0] - m
        
        l = 0
        r = n - 1
        while l<r:
            m = (l+r+1) >> 1
            c = count_missing(m)
            if c<k:
                l = m
            else:
                r = m - 1
        c = count_missing(l)
        left = k - c
        return nums[l] + left

def test(testObj: unittest.TestCase, nums: List[int], k: int, expected:int) -> None:
    
    so = Solution()
    actual = so.missingElement(nums,k)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [4,7,9,10],  1, 5)

    def test_2(self):
        test(self,   [4,7,9,10],  3, 8)

    def test_3(self):
        test(self,   [1,2,4],  3, 6)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 300 ms, faster than 93.12% of Python3 online submissions for Missing Element in Sorted Array.
Memory Usage: 20.1 MB, less than 86.89% of Python3 online submissions for Missing Element in Sorted Array.
'''

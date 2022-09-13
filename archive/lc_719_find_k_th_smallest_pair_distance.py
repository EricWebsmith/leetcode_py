from heapq import heappop, heappush
import unittest
from typing import Counter, List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected:int) -> None:
    
    so = Solution()
    
    actual = so.smallestDistancePair(nums, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,3,1],  1, 0)

    def test_2(self):
        test(self,   [1,1,1],  2, 0)

    def test_3(self):
        test(self,   [1,6,1],  3, 5)
    
    def test_4(self):
        test(self,   [1,6],  1, 5)
    
    def test_5(self):
        test(self,   [62,100,4], 2, 58)
    
    def test_6(self):
        test(self,   [0,0,0,1,1], 2, 0)
    

if __name__ == '__main__':
    unittest.main()

'''

'''

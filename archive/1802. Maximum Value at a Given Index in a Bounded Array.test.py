
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_sum(m):
            left = 0
            if m <= index + 1:
                left = (m +1) * m >> 1
                left += index+1-m
            else:
                arr0 = m - index
                left = (m + arr0) * (index + 1) >> 1
            right = 0
            if m<=n-index:
                right = (m + 1) * m >> 1
                right += n - (index + m)
            else:
                arr_last = m - (n-index-1)
                right = (m + arr_last) * (n - index) >> 1
            return left + right - m

        l = 1
        r = maxSum - n + 1
        while l<r:
            m = (l + r + 1) >> 1
            s = get_sum(m)
            if s<=maxSum:
                l = m
            else:
                r = m - 1
        
        return l


def test(testObj: unittest.TestCase, n: int, index: int, maxSum: int, expected:int) -> None:
    
    so = Solution()
    actual = so.maxValue(n,index,maxSum)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,   4,  2,  6, 2)

    def test_2(self):
        test(self,   6,  1,  10, 3)
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 43 ms, faster than 87.96% of Python3 online submissions for Maximum Value at a Given Index in a Bounded Array.
Memory Usage: 13.9 MB, less than 86.11% of Python3 online submissions for Maximum Value at a Given Index in a Bounded Array.
"""
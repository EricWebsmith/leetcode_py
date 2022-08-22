
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from utils.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from utils.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        current = sum(nums)
        ans = []
        for i in range(n):
            current -= nums[removeQueries[i]]
            ans.append(current)
        
        return ans


def test(testObj: unittest.TestCase, nums: List[int], removeQueries: List[int], expected:int) -> None:
    
    s = Solution()
    actual = s.maximumSegmentSum(nums,removeQueries)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  [1,2,5,6,1],  [0,3,2,4,1], [14,7,2,2,0])

    def test_2(self):
        test(self,  [3,2,11,1],  [3,2,1,0], [16,5,3,0])
    

if __name__ == '__main__':
    unittest.main()
        
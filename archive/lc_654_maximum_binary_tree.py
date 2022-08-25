from heapq import heappop, heappush
import unittest
from typing import List, Optional
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        max_value = 0
        index = 0
        for i in range(n):
            if nums[i]>max_value:
                max_value = nums[i]
                index = i
        
        node = TreeNode(max_value)
        node.left = self.constructMaximumBinaryTree(nums[:index]) 
        node.right = self.constructMaximumBinaryTree(nums[index+1:])
        return node

def test(testObj: unittest.TestCase, nums: List[int], expected:int) -> None:
    
    so = Solution()
    actual_root = so.constructMaximumBinaryTree(nums)
    actual = treenode_to_array(actual_root)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [3,2,1,6,0,5], [6,3,5,None,2,0,None,None,1])

    def test_2(self):
        test(self,   [3,2,1], [3,None,2,None,1])
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 226 ms, faster than 85.61% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.7 MB, less than 21.38% of Python3 online submissions for Maximum Binary Tree.
'''

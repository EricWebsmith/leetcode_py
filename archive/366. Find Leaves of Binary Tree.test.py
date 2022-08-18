
from heapq import heappop, heappush
import unittest
from typing import List, Optional
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from binary_tree import TreeNode, array_to_treenode

class Solution:

    def __init__(self):
        self.dict = {}

    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        level = max(left, right)+1
        if not level in self.dict:
            self.dict[level] = []
        self.dict[level].append(node.val)
        return level

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.dfs(root)
        keys = [k for k in self.dict.keys()]
        keys.sort()
        ans = []
        for key in keys:
            ans.append(self.dict[key])

        return ans


def test(testObj: unittest.TestCase, root_arr: List[int], expected:int) -> None:
    root = array_to_treenode(root_arr)
    s = Solution()
    actual = s.findLeaves(root)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  [1,2,3,4,5], [[4,5,3],[2],[1]])

    def test_2(self):
        test(self,  [1], [[1]])
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 43 ms, faster than 64.12% of Python3 online submissions for Find Leaves of Binary Tree.
Memory Usage: 14 MB, less than 26.76% of Python3 online submissions for Find Leaves of Binary Tree.
"""
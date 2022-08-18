
from heapq import heappop, heappush
import unittest
from typing import List, Optional
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from utils.binary_tree import TreeNode

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


def test(testObj: unittest.TestCase, root: Optional[TreeNode], expected:int) -> None:
    s = Solution()
    actual = s.findLeaves(root)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
        
    # def test_1(self):
    #     test(self,  [1,2,3,4,5], [[4,5,3],[2],[1]])

    def test_2(self):
        test(self,  [1], [[1]])
    

if __name__ == '__main__':
    unittest.main()
        
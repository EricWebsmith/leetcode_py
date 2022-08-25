
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
from math import sqrt

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(start, x):
            if cur:
                res.append(cur + [x])
            for factor in range(start, int(sqrt(x))+1):
                if x % factor == 0:
                    cur.append(factor)
                    backtrack(factor, x//factor)
                    cur.pop()

        backtrack(2, n)
        return res


def test(testObj: unittest.TestCase, n: int, expected:int) -> None:
    
    so = Solution()
    actual = so.getFactors(n)
    actual.sort()
    expected.sort()
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,   1, [])

    def test_2(self):
        test(self,   12, [[2,6],[3,4],[2,2,3]])

    def test_3(self):
        test(self,   37, [])
    

if __name__ == '__main__':
    unittest.main()
        
"""
Runtime: 130 ms, faster than 69.92% of Python3 online submissions for Factor Combinations.
Memory Usage: 15 MB, less than 52.72% of Python3 online submissions for Factor Combinations.
"""
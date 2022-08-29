from heapq import heappop, heappush
from queue import Queue
import unittest
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x!=self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def merge(self, x: int, y: int) -> int:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1
        
        self.p[px] = py
        self.e += 1
        return 0

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = DSU(n+1)
        B = DSU(n+1)
        ans = 0
        for t, x, y in edges:
            if t!=3:
                continue
            ans += A.merge(x, y)
            B.merge(x, y)
        
        for t, x, y in edges:
            if t == 3:
                continue
            d = A if t == 1 else B
            ans += d.merge(x, y)
        
        return ans if A.e == B.e == n-1 else -1

def test(testObj: unittest.TestCase, n: int, edges: List[List[int]], expected:int) -> None:
    
    so = Solution()
    actual = so.maxNumEdgesToRemove(n,edges)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   4,  [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]], 2)

    def test_2(self):
        test(self,   4,  [[3,1,2],[3,2,3],[1,1,4],[2,1,4]], 0)

    def test_3(self):
        test(self,   4,  [[3,2,3],[1,1,2],[2,3,4]], -1)
    

if __name__ == '__main__':
    unittest.main()

'''

'''

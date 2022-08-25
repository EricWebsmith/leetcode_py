
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
import numpy as np

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = np.zeros([4, m, n], dtype=int)
        HORIZONTAL = 0
        VERTICAL = 1
        DIAGONAL = 2
        ANTI_DIAGONAL = 3

        for r in range(m):

            for c in range(n):
                if mat[r][c] == 0:
                    continue

                dp[HORIZONTAL][r][c] = dp[HORIZONTAL][r][c-1] + 1 if c>0 else 1
                dp[VERTICAL][r][c] = dp[VERTICAL][r-1][c] + 1 if r>0 else 1
                dp[DIAGONAL][r][c] = dp[DIAGONAL][r-1][c-1] + 1 if r>0 and c>0 else 1

            for c in range(n-1, -1, -1):
                if mat[r][c] == 0:
                    continue
                dp[ANTI_DIAGONAL][r][c] = (dp[ANTI_DIAGONAL][r-1][c+1] + 1) if (c<n-1 and r>0) else 1

        return np.max(dp)


def test(testObj: unittest.TestCase, mat: List[List[int]], expected:int) -> None:
    
    so = Solution()
    actual = so.longestLine(mat)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,   [[0,1,1,0],[0,1,1,0],[0,0,0,1]], 3)

    def test_2(self):
        test(self,   [[1,1,1,1],[0,1,1,0],[0,0,0,1]], 4)
    

if __name__ == '__main__':
    unittest.main()
        
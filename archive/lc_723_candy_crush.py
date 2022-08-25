
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Tuple
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
import numpy as np


class Solution:
    def __init__(self) -> None:
        self.m = 0
        self.n = 0

    def label(self, board: List[List[int]]):
        found = False
        for r in range(self.m):
            for c in range(self.n-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    found = True

        for c in range(self.n):
            for r in range(self.m-2):
            
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    found = True

        return found

    def crush(self, board):
        # bottom up
        for c in range(self.n):
            down = 0
            for r in range(self.m-1, -1, -1):
                if board[r][c] < 0:
                    down+=1
                elif down>0:
                    board[r+down][c] = board[r][c]
            
            for r in range(0, down):
                board[r][c] = 0

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.m = len(board)
        self.n = len(board[0])

        found = self.label(board)
        while found:
            self.crush(board)
            found = self.label(board)

        return board


def test(testObj: unittest.TestCase, board: List[List[int]], expected:int) -> None:
    
    so = Solution()
    actual = so.candyCrush(board)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   
            [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]], 
            [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]])

    def test_2(self):
        test(self,   
            [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]], 
            [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]])
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 252 ms, faster than 63.37% of Python3 online submissions for Candy Crush.
Memory Usage: 14.1 MB, less than 54.02% of Python3 online submissions for Candy Crush.
"""
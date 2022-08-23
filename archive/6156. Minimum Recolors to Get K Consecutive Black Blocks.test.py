
from heapq import heappop, heappush
from turtle import right
import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        current = 0

        for i in range(k):
            if blocks[i] == 'W':
                current += 1
        
        final = current

        for i in range(k, n):
            if blocks[i] == 'W':
                current += 1
            if blocks[i-k] == 'W':
                current -= 1
            final = min(current, final)

        return final


def test(testObj: unittest.TestCase, blocks: str, k: int, expected:int) -> None:
    
    s = Solution()
    actual = s.minimumRecolors(blocks,k)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  "WBBWWBBWBW",  7, 3)

    def test_2(self):
        test(self,  "WBWBBBW",  2, 0)
    

if __name__ == '__main__':
    unittest.main()
        
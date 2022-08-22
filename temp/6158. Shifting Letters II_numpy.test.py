
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indices = [letters.index(ss) for ss in s]
        indices = np.array(indices)

        for start, end, direction in shifts:
            if direction == 0:
                indices[start: end+1] = indices[start: end+1] - 1
                # for i in range(start , end+1):
                #     if indices[i] == 0:
                #         indices[i] = 25
                #     else:
                #         indices[i] = indices[i] - 1
                    
            else:
                indices[start: end+1] = indices[start: end+1] + 1
                # for i in range(start , end+1):
                #     if indices[i] == 25:
                #         indices[i] = 0
                #     else:
                #         indices[i] = indices[i] + 1

        ans = "".join([letters[(i + 2600000) % 26] for i in indices])
        return ans


def test(testObj: unittest.TestCase, s: str, shifts: List[List[int]], expected:int) -> None:
    
    so = Solution()
    actual = so.shiftingLetters(s,shifts)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  "abc",  [[0,1,0],[1,2,1],[0,2,1]], "ace")

    def test_2(self):
        test(self,  "dztz",  [[0,0,0],[1,1,1]], "catz")
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 9256 ms, faster than 20.00% of Python3 online submissions for Shifting Letters II.
Memory Usage: 57.3 MB, less than 40.00% of Python3 online submissions for Shifting Letters II.
"""        
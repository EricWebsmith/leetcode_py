
from heapq import heappop, heappush
import re
import unittest
from typing import List, Optional
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from binary_tree import TreeNode, array_to_treenode

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        results = []
        for i in range(n):
            result = 0
            for j in range(i):
                if boxes[j] == '1':
                    result += i-j
            for j in range(i+1, n):
                if boxes[j] == '1':
                    result += j-i
            results.append(result)

        return results


def test(testObj: unittest.TestCase, boxes: str, expected:int) -> None:
    
    s = Solution()
    actual = s.minOperations(boxes)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  "110", [1,1,3])

    def test_2(self):
        test(self,  "001011", [11,8,5,4,3,4])
    

if __name__ == '__main__':
    unittest.main()
        
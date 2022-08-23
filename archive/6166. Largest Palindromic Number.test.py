
from heapq import heappop, heappush
import unittest
from typing import Counter, List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def largestPalindromic(self, num: str) -> str:
        l = list(num)
        c = Counter(l)
        left = []
        right = []
        mid = ''
        for key in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']:
            
            if key == '0' and len(left) == 0 and mid != '':
                return mid
            if key == '0' and len(left) == 0: 
                return '0'

            if c[key] > 0:
                half = c[key] // 2
                left = left + [key] * half
                right = [key] * half + right
                if mid == '' and c[key] - 2 * half == 1:
                    mid = key

        return ''.join(left+[mid]+right)


def test(testObj: unittest.TestCase, num: str, expected:int) -> None:
    
    so = Solution()
    actual = so.largestPalindromic(num)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    # def test_1(self):
    #     test(self,  "444947137", "7449447")

    def test_2(self):
        test(self,  "00009", "9")
    

if __name__ == '__main__':
    unittest.main()
        
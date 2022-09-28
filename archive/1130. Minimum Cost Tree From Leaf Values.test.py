
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0

        while len(arr)>1:
            min_product = arr[0] * arr[1]
            min_product_at = 0
            for i in range(1, len(arr)-1):
                current = arr[i] * arr[i+1]
                if current < min_product:
                    min_product = current
                    min_product_at = i
            
            ans += min_product
            arr = arr[:min_product_at] +[max(arr[min_product_at], arr[min_product_at+1])]+ arr[min_product_at+2:]

        return ans


def test(testObj: unittest.TestCase, arr: List[int], expected:int) -> None:
    
    so = Solution()
    actual = so.mctFromLeafValues(arr)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,   [6,2,4], 32)

    def test_2(self):
        test(self,   [4,11], 44)
    
    def test_3(self):
        test(self,   [1,2,3,4,5], 40)
    
    def test_4(self):
        test(self,   [1,1, 1], 2)
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 48 ms, faster than 75.73% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
Memory Usage: 14 MB, less than 47.33% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
"""

import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def get_sum(self, arr: List[int], threshold: int):
        sum = 0
        for i in range(len(arr)):
            if arr[i]>=threshold:
                sum += threshold
            else:
                sum += arr[i]
        return sum

    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l = target // n - 1
        r = max(arr)

        while l<r:
            m = (l + r) // 2
            s = self.get_sum(arr, m)
            if s<target:
                l = m + 1
            else:
                r = m
        
        l_value = target - self.get_sum(arr, l-1)
        r_value = self.get_sum(arr, l)-target
        if l_value <= r_value:
            return l-1
        else:
            return l


def test(testObj: unittest.TestCase, arr: List[int], target: int, expected:int) -> None:
    
    so = Solution()
    actual = so.findBestValue(arr,target)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self, [4,9,3],  10, 3)

    def test_2(self):
        test(self, [2,3,5],  10, 5)

    def test_3(self):
        test(self, [60864,25176,27249,21296,20204],  56803, 11361)
    

if __name__ == '__main__':
    unittest.main()
        
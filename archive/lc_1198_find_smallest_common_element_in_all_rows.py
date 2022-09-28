import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        last_row = mat.pop()
        n = len(last_row)
        m = len(mat)
        if m == 0:
            return last_row[0]
        
        indicies = [0] * m
        for c in range(n):
            target = last_row[c]
            found = 0
            for r in range(m):
                while indicies[r]<n and mat[r][indicies[r]]<target:
                    indicies[r] += 1
                if indicies[r] == n:
                    return -1
                if mat[r][indicies[r]] != target:
                    break
                
                found += 1
            
            if found == m:
                return target


        return -1



def test(testObj: unittest.TestCase, mat: List[List[int]], expected:int) -> None:
    
    so = Solution()
    actual = so.smallestCommonElement(mat)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]], 5)

    def test_2(self):
        test(self,   [[1,2,3],[2,3,4],[2,3,5]], 2)
    
    def test_3(self):
        test(self,   [[1,2,3],[2,3,4],[2,3,5], [3,4,5]], 3)
    
    def test_4(self):
        test(self,   [[1,2,3],[2,3,4],[2,3,5], [3,4,5], [4, 5, 6]], -1)
    
    def test_5(self):
        test(self,   [[1,2,3], [4,5,6]], -1)
    
    def test_6(self):
        test(self,   [[1,2,3]], 1)
    
if __name__ == '__main__':
    unittest.main()

'''
Runtime: 516 ms, faster than 94.33% of Python3 online submissions for Find Smallest Common Element in All Rows.
Memory Usage: 39 MB, less than 55.52% of Python3 online submissions for Find Smallest Common Element in All Rows.
'''

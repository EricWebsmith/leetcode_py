
from heapq import heappop, heappush
import unittest
from typing import List, Optional
from utils.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from utils.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        hours = 0
        n = len(energy)
        ene = initialEnergy
        exp = initialExperience
        for i in range(n):
            if energy[i] >= ene:
                hours += energy[i] - ene + 1
                ene = energy[i] + 1
            if experience[i] >= exp:
                hours += experience[i] - exp +1 
                exp = experience[i]+1
            
            ene -= energy[i]
            exp += experience[i]

        return hours


def test(testObj: unittest.TestCase, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int], expected:int) -> None:
    
    so = Solution()
    actual = so.minNumberOfHours(initialEnergy,initialExperience,energy,experience)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  5,  3,  [1,4,3,2],  [2,6,3,1], 8)

    def test_2(self):
        test(self,  2,  4,  [1],  [3], 0)

    def test_3(self):
        test(self,  1, 1, [1,1,1,1], [1,1,1,50], 51)
    

if __name__ == '__main__':
    unittest.main()
        
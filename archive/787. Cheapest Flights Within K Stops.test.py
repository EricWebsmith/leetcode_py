
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
         
        for i in range(k+1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                tmpPrices[d] =min(tmpPrices[d], prices[s] + p) 
        
            prices = tmpPrices

        return -1 if prices[dst] == float('inf') else prices[dst] 


def test(testObj: unittest.TestCase, n: int, flights: List[List[int]], src: int, dst: int, k: int, expected:int) -> None:
    
    s = Solution()
    actual = s.findCheapestPrice(n,flights,src,dst,k)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  4,  [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],  0,  3,  1, 700)

    def test_2(self):
        test(self,  3,  [[0,1,100],[1,2,100],[0,2,500]],  0,  2,  1, 200)

    def test_3(self):
        test(self,  3,  [[0,1,100],[1,2,100],[0,2,500]],  0,  2,  0, 500)
    

if __name__ == '__main__':
    unittest.main()
        
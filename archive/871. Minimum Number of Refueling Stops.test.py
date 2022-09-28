
# from heapq import heappop, heappush
import heapq
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append([target, float('inf')])
        tank = startFuel

        ans = 0
        prev_location = 0
        for location, capacity in stations:
            tank -= location -prev_location
            while pq and tank < 0:
                tank+= - heapq.heappop(pq)
                ans += 1
            if tank < 0:
                return -1
            
            heapq.heappush(pq, -capacity)
            prev_location = location

        return ans


def test(testObj: unittest.TestCase, target: int, startFuel: int, stations: List[List[int]], expected:int) -> None:
    
    s = Solution()
    actual = s.minRefuelStops(target,startFuel,stations)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  1,  1,  [], 0)

    def test_2(self):
        test(self,  100,  1,  [[10,100]], -1)

    def test_3(self):
        test(self,  100,  10,  [[10,60],[20,30],[30,30],[60,40]], 2)
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 162 ms, faster than 78.41% of Python3 online submissions for Minimum Number of Refueling Stops.
Memory Usage: 14.3 MB, less than 10.13% of Python3 online submissions for Minimum Number of Refueling Stops.
"""

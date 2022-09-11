from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class HitCounter:

    def __init__(self):
        self.hits = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp]+=1

    def getHits(self, timestamp: int) -> int:
        keys = list(self.hits.keys())
        for k in keys:
            if k<=timestamp-300:
                del self.hits[k]
        
        return sum(self.hits.values())


def test(testObj: unittest.TestCase, actions:List, params:List , expected:List) -> None:
    n = len(actions)
    obj = HitCounter(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:
            

            case "hit":
                actual = obj.hit(*params[i])
                testObj.assertEqual(actual, expected[i])
            
            case "getHits":
                actual = obj.getHits(*params[i])
                testObj.assertEqual(actual, expected[i])
            
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self, ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"], [[], [1], [2], [3], [4], [300], [300], [301]], [None, None, None, None, 3, None, 4, 3])
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 35 ms, faster than 88.20% of Python3 online submissions for Design Hit Counter.
Memory Usage: 14 MB, less than 59.91% of Python3 online submissions for Design Hit Counter.
'''

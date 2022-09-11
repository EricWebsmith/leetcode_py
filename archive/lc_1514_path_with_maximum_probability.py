from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


def get_bidirectional_edges(vetices: List, from_tos: List[List], weights: List[float]) -> Dict[Any, Set]:
    edges = {v: set() for v in vetices}
    for (from_, to_), w in zip(from_tos, weights):
        edges[from_].add((to_, w))
        edges[to_].add((from_, w))

    return edges


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        bi_edges = get_bidirectional_edges(list(range(n)), edges, succProb)
        h = [(-1, start)]
        dp = [0] * n
        
        while h:
            probability, current = heappop(h)
            probability = -probability
            for next, w in bi_edges[current]:
                next_pro = probability * w
                if next_pro > dp[next]:
                    dp[next] = next_pro
                    heappush(h, (-next_pro, next))
                if next_pro == end:
                    break

        return dp[end]



def test(testObj: unittest.TestCase, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int, expected:float) -> None:
    
    so = Solution()
    
    actual = so.maxProbability(n,edges,succProb,start,end)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   3,  [[0,1],[1,2],[0,2]],  [0.5,0.5,0.2],  0,  2, 0.25000)

    def test_2(self):
        test(self,   3,  [[0,1],[1,2],[0,2]],  [0.5,0.5,0.3],  0,  2, 0.30000)

    def test_3(self):
        test(self,   3,  [[0,1]],  [0.5],  0,  2, 0.00000)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 782 ms, faster than 87.53% of Python3 online submissions for Path with Maximum Probability.
Memory Usage: 26.8 MB, less than 38.54% of Python3 online submissions for Path with Maximum Probability.
'''

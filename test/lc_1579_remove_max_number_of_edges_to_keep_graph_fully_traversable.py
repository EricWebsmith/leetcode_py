from heapq import heappop, heappush
from queue import Queue
import unittest
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

def get_bidirectional_edges(vetices: List, from_tos: List[List]) -> Dict[Any, Set]:
    edges = {v: set() for v in vetices}
    for from_, to_ in from_tos:
        edges[from_].add(to_)
        edges[to_].add(from_)
    
    return edges

def traverse(vetices: List, edges: Dict[Any, Set[Any]]):
    visited = set()
    q = Queue()
    q.put(vetices[0])

    while q.qsize()>0:
        v = q.get()
        if v in visited:
            return

        visited.add(v)

        for neighbor in edges[v]:
            q.put(neighbor)

    return len(visited) == len(vetices)

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        vetices = list(range(1, n+1))
        alice_connectoins = [[a, b] for type, a, b in edges if type==1]
        bob_connections = [[a, b] for type, a, b in edges if type==2]
        shared_connections = [[a, b] for type, a, b in edges if type==3]
        alice_edges = get_bidirectional_edges(vetices, alice_connectoins + shared_connections)
        if not traverse(alice_edges):
            return -1
        
        bob_edges = get_bidirectional_edges(vetices, shared_connections + shared_connections)
        if not traverse(bob_edges):
            return -1

        alice_ans = len(alice_connectoins) + len(shared_connections) - len(vetices) - 1
        # continue at home

def test(testObj: unittest.TestCase, n: int, edges: List[List[int]], expected:int) -> None:
    
    so = Solution()
    actual = so.maxNumEdgesToRemove(n,edges)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   4,  [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]], 2)

    def test_2(self):
        test(self,   4,  [[3,1,2],[3,2,3],[1,1,4],[2,1,4]], 0)

    def test_3(self):
        test(self,   4,  [[3,2,3],[1,1,2],[2,3,4]], -1)
    

if __name__ == '__main__':
    unittest.main()

'''

'''

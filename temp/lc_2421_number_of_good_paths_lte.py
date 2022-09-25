
from heapq import heappop, heappush
import unittest
from functools import cache
from itertools import combinations
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
null = None


from dataclasses import dataclass


def get_bidirectional_edges(vetices: List, from_tos: List[List]) -> Dict[Any, Set]:
    edges = {v: set() for v in vetices}
    for from_, to_ in from_tos:
        edges[from_].add(to_)
        edges[to_].add(from_)

    return edges


@dataclass
class Node:
    index: int = -1
    parent: 'Node' = None

    def __repr__(self) -> str:

        if self.parent:
            return f'{self.index} -> {self.parent.index}'
        return f'{self.index} root'


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        bidirectional_edges = get_bidirectional_edges(list(range(n)), edges)
        nodes = [None] * n
        root = Node(0)
        nodes[0] = root
        q = [(root, -1)]
        while q:
            new_q = []
            while q:
                node, parent_index = q.pop()
                for v in bidirectional_edges[node.index]:
                    if v == parent_index:
                        continue
                    child = Node(v)
                    nodes[v] = child
                    child.parent = node
                    new_q.append((child, node.index))
            q = new_q

        lca = [i for i in range(n)]
        for i in range(n):
            node = nodes[i]
            val = vals[i]
            parent = node.parent

            while parent:
                if vals[parent.index] <= val:
                    lca[i] = parent.index
                else:
                    break
                parent = parent.parent

        ans = 0

        val_index_dict = defaultdict(list)
        for i in range(n):
            val_index_dict[vals[i]].append(i)
        
        for val, indices in val_index_dict.items():
            for i, j in combinations(indices, 2):
                if lca[i] == lca[j]:
                    ans += 1

        return ans + n


def test(testObj: unittest.TestCase, vals: List[int], edges: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.numberOfGoodPaths(vals, edges)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3, 2, 1, 3],  [[0, 1], [0, 2], [2, 3], [2, 4]], 6)

    def test_2(self):
        test(self,   [1, 1, 2, 2, 3],  [[0, 1], [1, 2], [2, 3], [2, 4]], 7)

    def test_3(self):
        test(self,   [1],  [], 1)


if __name__ == '__main__':
    unittest.main()

'''
Time Limit Exceeded
'''

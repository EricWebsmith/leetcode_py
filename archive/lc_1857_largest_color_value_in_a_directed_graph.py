from heapq import heappop, heappush
import unittest
from typing import Counter, List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


def get_edges(n: int, from_tos: List[List[int]]) -> Dict[int, Set[int]]:
    edges = {i: set() for i in range(n)}
    for from_, to_ in from_tos:
        edges[from_].add(to_)

    return edges


class Solution:
    def __init__(self) -> None:
        self.circle = False
        self.best_count = 1
        self.color_bag = [0] * 26

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        visited = [False] * n
        visiting = [False] * n

        directed_edges = get_edges(n, edges)

        color_indices = [ord(c)-97 for c in colors]

        start_positions = set(range(n))
        for edge in edges:
            if edge[1] in start_positions:
                start_positions.remove(edge[1])

        if len(start_positions) == 0:
            return -1

        def back_track(i: int):
            visited[i] = True
            if self.circle:
                return

            if visiting[i]:
                self.circle = True
                return

            visiting[i] = True

            tos = directed_edges[i]
            for to in tos:
                self.color_bag[color_indices[to]] += 1
                back_track(to)
                self.color_bag[color_indices[to]] -= 1

            if len(tos) == 0:
                self.best_count = max(self.best_count,  max(self.color_bag))

            visiting[i] = False

        for i in start_positions:
            self.color_bag[color_indices[i]] += 1
            back_track(i)
            self.color_bag[color_indices[i]] -= 1

        if self.circle:
            return -1

        return self.best_count


def test(testObj: unittest.TestCase, colors: str, edges: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.largestPathValue(colors, edges)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "abaca",  [[0, 1], [0, 2], [2, 3], [3, 4]], 3)

    def test_2(self):
        test(self,   "a",  [[0, 0]], -1)

    def test_3(self):
        test(self,   "abbcc", [[0, 1], [1, 2], [0, 3], [3, 4]], 2)

    def test_4(self):
        test(self,   "abbcc", [], 1)

    def test_5(self):
        test(self,   "vwnnvwvqvq",
             [[0, 1], [0, 2], [2, 3], [3, 4], [4, 5], [5, 6], [5, 7], [7, 8], [6, 9]], 3)

    def test_6(self):
        test(self,   "hhqhuqhqff",
             [[0, 1], [0, 2], [2, 3], [3, 4], [3, 5], [5, 6], [2, 7], [6, 7], [7, 8], [3, 8], [5, 8], [8, 9], [3, 9], [6, 9]], 3)

    def test_7(self):
        test(self,   "ccbba", [[1, 0], [4, 3], [3, 2], [4, 1]], 2)


if __name__ == '__main__':
    unittest.main()

'''
TLE
'''

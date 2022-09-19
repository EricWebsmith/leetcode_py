from bisect import bisect_left, insort_left
from heapq import heappop, heappush
from re import L
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        n = len(arrival)
        if k == 1:
            return [0]

        if k >= n:
            return list(range(n))

        idle_servers = list(range(k))
        busy_servers = []
        handler_dict = defaultdict(int)
        for i, start_time, span in zip(range(n), arrival, load):
            while busy_servers and busy_servers[-1][0] <= start_time:
                _, old_busy_server = busy_servers.pop()
                insort_left(idle_servers, old_busy_server)
            if len(idle_servers) == 0:
                continue
            first_server = i % k
            handler_index = bisect_left(idle_servers, first_server)
            handler_index = handler_index % len(idle_servers)
            handler = idle_servers[handler_index]
            handler_dict[handler] += 1
            del idle_servers[handler_index]
            end_time = start_time + span
            insort_left(busy_servers, x=(
                end_time, handler), key=lambda x: -x[0])

        max_serves = max(handler_dict.values())
        ans = []
        for server,  serves in handler_dict.items():
            if max_serves == serves:
                ans.append(server)

        return ans


def test(testObj: unittest.TestCase, k: int, arrival: List[int], load: List[int], expected: List[int]) -> None:

    so = Solution()

    actual = so.busiestServers(k, arrival, load)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   3,  [1, 2, 3, 4, 5],  [5, 2, 3, 3, 3], [1])

    def test_2(self):
        test(self,   3,  [1, 2, 3, 4],  [1, 2, 1, 2], [0])

    def test_3(self):
        test(self,   3,  [1, 2, 3],  [10, 12, 11], [0, 1, 2])

    def test_4(self):
        test(self,   3,  [1],  [10], [0])

    def test_5(self):
        test(self,   3,  [1, 2, 3, 4, 5],  [10, 12, 11, 1, 2], [0, 1, 2])

    def test_6(self):
        test(self,   1,  [1, 2, 3, 4, 5],  [5, 2, 3, 3, 3], [0])

    def test_7(self):
        test(self,   1,  [1],  [5], [0])

    def test_8(self):
        test(self,   3,  [1, 2, 3, 4, 5],  [5000, 2000, 1, 1, 1], [2])

    def test_9(self):
        test(self,   3, [1, 2, 3, 4, 8, 9, 10], [5, 2, 10, 3, 1, 2, 2], [1])


if __name__ == '__main__':
    unittest.main()

'''

'''

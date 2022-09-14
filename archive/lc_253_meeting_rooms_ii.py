from bisect import bisect_left
from heapq import heapify, heappop, heappush
import unittest
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms: List[List[int]] = []
        intervals.sort(key=lambda x: x[0])
        heappush(rooms, intervals[0][1])
        for start, end in intervals[1:]:
            if rooms[0] <= start:
                heappop(rooms)
            
            heappush(rooms, end)


        return len(rooms)


def test(testObj: unittest.TestCase, intervals: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.minMeetingRooms(intervals)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 30], [5, 10], [15, 20]], 2)

    def test_2(self):
        test(self,   [[7, 10], [2, 4]], 1)

    def test_3(self):
        test(self,   [[2,15],[36,45],[9,29],[16,23],[4,9]], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 86 ms, faster than 89.95% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 17.5 MB, less than 83.51% of Python3 online submissions for Meeting Rooms II.
'''

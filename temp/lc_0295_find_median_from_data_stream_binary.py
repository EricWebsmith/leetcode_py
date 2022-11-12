import unittest
from bisect import bisect_left, insort_left
from collections import defaultdict, deque
from functools import cache
from heapq import heappop, heappush
from math import sqrt
from typing import Any, Dict, List, Optional, Set

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)
from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)
from data_structure.nary_tree import Node, array_to_node, node_to_array

null = None


class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        insort_left(self.arr, num)

    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2 == 1:
            return self.arr[l//2]
        else:
            return (self.arr[l//2] + self.arr[l//2 - 1])/2


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = MedianFinder(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "addNum":
                actual = obj.addNum(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "findMedian":
                actual = obj.findMedian(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [
             [], [1], [2], [], [3], []], [None, None, None, 1.5, None, 2.0])


if __name__ == '__main__':
    unittest.main()

'''

'''

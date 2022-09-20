from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class RangeModule:

    def __init__(self):
        # we treat ranges as time spans
        # because range is a python keyword.
        self.spans = []

    def addRange(self, left: int, right: int) -> None:
        index = bisect_left(self.spans, x=left, key=lambda x: x[0])
        # merge with next
        if index < len(self.spans) and right >= self.spans[index][0]:
            right = self.spans[index][1]
            del self.spans[index]
        if index > 0 and left <= self.spans[index-1][1]:
            left = self.spans[index-1][0]
            del self.spans[index-1]
            index -= 1

        self.spans.insert(index, (left, right))

    def queryRange(self, left: int, right: int) -> bool:
        index = bisect_right(self.spans, x=left, key=lambda x: x[0])
        if index == 0:
            return False
        if self.spans[index-1][1] >= right:
            return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        left_index = bisect_right(self.spans, x=left, key=lambda x: x[1])
        right_index = bisect_right(self.spans, x=right, key=lambda x: x[0])
        if left_index+1 == right_index:
            span1 = (self.spans[left_index][0], left)
            span2 = (right, self.spans[left_index][1])
            del self.spans[left_index]
            self.spans.insert(left_index, span2)
            self.spans.insert(left_index, span1)
            return
        self.spans = self.spans[0:left_index+1] + self.spans[right_index-1:]
        if self.spans[left_index][1] > left:
            self.spans[left_index] = (self.spans[left_index][0], left)
        if left_index+1 < len(self.spans) and self.spans[left_index+1][0] < right:
            self.spans[left_index+1] = (right, self.spans[left_index+1][1])


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = RangeModule(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "addRange":
                actual = obj.addRange(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "queryRange":
                actual = obj.queryRange(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "removeRange":
                actual = obj.removeRange(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"], [
             [], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]], [None, None, None, True, False, True])

    def test_2(self):
        test(self, ["RangeModule", "addRange", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"], [
             [], [10, 20], [30, 40], [15, 35], [10, 14], [13, 15], [16, 17]], [None, None, None, None, True, True, False])


if __name__ == '__main__':
    unittest.main()

'''

'''

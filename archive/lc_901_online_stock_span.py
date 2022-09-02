from bisect import bisect_left, bisect_right, insort_right
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class StockSpanner:

    def __init__(self):
        self.arr = []
        self.dp = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        n = len(self.arr)
        if n == 1:
            self.dp.append(1)
            return 1

        prev = n-2
        while prev >= 0 and self.arr[prev] <= price:
            prev -= self.dp[prev]

        ans = n-prev-1
        self.dp.append(ans)
        return ans


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = StockSpanner(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:
            case "next":
                actual = obj.next(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"], [
             [], [100], [80], [60], [70], [60], [75], [85]], [None, 1, 1, 1, 2, 1, 4, 6])

    def test_2(self):
        test(self,
             ["StockSpanner", "next", "next", "next", "next", "next"],
             [[], [31], [41], [48], [59], [79]],
             [None, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 448 ms, faster than 89.53% of Python3 online submissions for Online Stock Span.
Memory Usage: 19.7 MB, less than 7.77% of Python3 online submissions for Online Stock Span.
'''

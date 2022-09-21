import random
from bisect import bisect_right
from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:

    def __init__(self, n: int, blocklist: List[int]):
        blocklist.sort()
        self.n = n
        self.blocklist = blocklist

    def pick(self) -> int:
        m = len(self.blocklist)
        v = random.randint(0, self.n-m-1)
        l = 0
        r = m
        while l < r:
            m = (l + r) >> 1
            if v + m >= self.blocklist[m]:
                l = m + 1
            else:
                r = m

        return v + r


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = Solution(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):

        match actions[i]:

            case "pick":
                actual = obj.pick(*params[i])
                print(i, actions[i], params[i], expected[i], actual)
                # testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"], [
             [7, [2, 3, 5]], [], [], [], [], [], [], []], [None, 0, 4, 1, 6, 1, 0, 4])

    def test_2(self):
        test(self, ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"], [
             [4, [2, 1]], [], [], [], [], [], [], []], [None, 0, 4, 1, 6, 1, 0, 4])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 492 ms, faster than 55.74% of Python3 online submissions for Random Pick with Blacklist.
Memory Usage: 23.4 MB, less than 95.29% of Python3 online submissions for Random Pick with Blacklist.
'''

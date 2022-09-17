from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class MRUQueue:

    def __init__(self, n: int):
        self.arr = [i+1 for i in range(n)]

    def fetch(self, k: int) -> int:
        ans = self.arr[k-1]
        del self.arr[k - 1]
        self.arr.append(ans)
        return ans


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = MRUQueue(*params[0])
    for i in range(1, n):

        match actions[i]:

            case "fetch":
                actual = obj.fetch(*params[i])
                testObj.assertEqual(actual, expected[i])
        print(i, actions[i], params[i], expected[i], obj.arr)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["MRUQueue", "fetch", "fetch", "fetch", "fetch"], [
             [8], [3], [5], [2], [8]], [None, 3, 6, 2, 2])

    def test_2(self):
        test(self, ["MRUQueue", "fetch", "fetch", "fetch", "fetch", "fetch", "fetch", "fetch", "fetch", "fetch", "fetch"],
             [[3], [2], [1], [2], [2], [2], [3], [2], [1], [1], [2]],
             [null, 2, 1, 2, 1, 2, 2, 1, 3, 2, 3])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 352 ms, faster than 61.97% of Python3 online submissions for Design Most Recently Used Queue.
Memory Usage: 15.1 MB, less than 63.03% of Python3 online submissions for Design Most Recently Used Queue.
'''

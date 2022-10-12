from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
from data_structure.link_list import ListNode, listnode_to_array, array_to_listnode
null = None


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        o = [ord(s[i])-ord('a') for i in range(n)]
        ans = 1
        for length in range(1, n):
            left = 0
            right = left + length - 1
            values = set()
            v = 0
            for i in range(length):
                v *= 26
                v += o[i]
            values.add(v)

            while right+1 < n:
                v -= o[left] * (26 ** (length - 1))
                v *= 26
                v += o[right+1]
                values.add(v)
                left += 1
                right += 1
            ans += len(values)

        return ans


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()
    actual = so.distinctSubseqII(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "abc", 7)

    def test_2(self):
        test(self,   "aba", 6)

    def test_3(self):
        test(self,   "aaa", 3)

    def test_4(self):
        test(self,   "lee", 5)


if __name__ == '__main__':
    unittest.main()

'''

'''

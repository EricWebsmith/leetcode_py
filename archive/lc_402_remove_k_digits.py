from contextlib import nullcontext
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
import re


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            # if k == 0:
            #     break
            if stack or c != '0':
                stack.append(c)

        if k:
            stack = stack[:-k]

        ans = ''.join(stack)
        if ans == '':
            ans = '0'

        return ans


def test(testObj: unittest.TestCase, num: str, k: int, expected: int) -> None:

    so = Solution()
    actual = so.removeKdigits(num, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "1432219",  3, "1219")

    def test_2(self):
        test(self,   "10200",  1, "200")

    def test_3(self):
        test(self,   "10",  2, "0")

    def test_4(self):
        test(self,   "100",  2, "0")

    def test_5(self):
        test(self,   "12345",  1, "1234")


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 69 ms, faster than 95.38% of Python3 online submissions for Remove K Digits.
Memory Usage: 15.5 MB, less than 42.47% of Python3 online submissions for Remove K Digits.
'''

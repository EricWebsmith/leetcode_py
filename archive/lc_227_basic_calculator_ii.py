from heapq import heappop, heappush
from os import curdir
from select import select
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def __init__(self) -> None:
        self.stack: List[int] = []
        self.op = ''
        self.current = 0

    def operate(self, new_op):
        if self.op == '*':
            self.current = self.stack.pop() * self.current
        elif self.op == '/':
            t = self.stack.pop()
            if t >= 0:
                self.current = t // self.current
            else:
                self.current = -(-t // self.current)
        else:
            self.stack = [sum(self.stack)]

        self.op = new_op
        self.stack.append(self.current)
        self.current = 0

    def calculate(self, s: str) -> int:
        for c in s+'+':
            if '0' <= c <= '9':
                t = int(c)
                if self.op == '-':
                    t = -t

                self.current = self.current * 10 + t
            elif c in '+-*/':
                self.operate(c)

        return sum(self.stack)


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()

    actual = so.calculate(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "3+2*2", 7)

    def test_2(self):
        test(self,   " 3/2 ", 1)

    def test_3(self):
        test(self,   " 3+5 / 2 ", 5)

    def test_4(self):
        test(self,   "14-3/2", 13)


if __name__ == '__main__':
    unittest.main()

'''

'''

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
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        i = 0
        while i < n:
            if dominoes[i] != '.':
                j = i + 1
                while j < n and dominoes[j] == '.':
                    j += 1

                if j == n:
                    break

                if dominoes[i] == dominoes[j]:
                    dominoes[i:j+1] = [dominoes[i]] * (j-i+1)

                if dominoes[i] == 'R' and dominoes[j] == 'L':
                    left = i + 1
                    right = j - 1
                    while left < right:
                        dominoes[left] = 'R'
                        dominoes[right] = 'L'

                        left += 1
                        right -= 1

                i = j
            else:
                i += 1
        # left
        i = 0
        while i < n-1 and dominoes[i] == '.':
            i += 1

        if dominoes[i] == 'L':
            dominoes[:i] = ['L'] * i

        # right
        i = n-1
        while i > 0 and dominoes[i] == '.':
            i -= 1

        if dominoes[i] == 'R':
            dominoes[i:] = ['R'] * (n-i)

        return ''.join(dominoes)


def test(testObj: unittest.TestCase, dominoes: str, expected: str) -> None:
    so = Solution()
    actual = so.pushDominoes(dominoes)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "RR.L", "RR.L")

    def test_2(self):
        test(self,   ".L.R...LR..L..", "LL.RR.LLRRLL..")

    def test_3(self):
        test(self,   "LL.RR.LLRRLL..", "LL.RR.LLRRLL..")

    def test_4(self):
        test(self,   "L...", "L...")

    def test_5(self):
        test(self,   "R...", "RRRR")

    def test_6(self):
        test(self,   "...L", "LLLL")

    def test_7(self):
        test(self,   "...R", "...R")

    def test_8(self):
        test(self,   ".", ".")

    def test_9(self):
        test(self,   "R", "R")

    def test_10(self):
        test(self,   "L", "L")


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 507 ms, faster than 57.48% of Python3 online submissions for Push Dominoes.
Memory Usage: 15.8 MB, less than 83.88% of Python3 online submissions for Push Dominoes.
'''

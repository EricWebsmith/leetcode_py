import unittest
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


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n_bits_2 = 0
        while num2 > 0:
            if num2 & 1 == 1:
                n_bits_2 += 1
            num2 >>= 1

        n_bits_1 = 0
        num1_copy = num1
        while num1_copy > 0:
            if num1_copy & 1 == 1:
                n_bits_1 += 1
            num1_copy >>= 1

        if n_bits_1 == n_bits_2:
            return num1

        if n_bits_1 < n_bits_2:
            ans = num1
            bits_diff = n_bits_2 - n_bits_1
            mask = 1
            k = 0
            while k < bits_diff:
                if mask & ans == 0:
                    ans += mask
                    k += 1
                mask <<= 1

            return ans

        if n_bits_1 > n_bits_2:
            ans = num1
            bits_diff = n_bits_1 - n_bits_2
            mask = 1
            k = 0
            while k < bits_diff:
                if mask & ans > 0:
                    ans -= mask
                    k += 1
                mask <<= 1

            return ans


def test(testObj: unittest.TestCase, num1: int, num2: int, expected: int) -> None:

    so = Solution()

    actual = so.minimizeXor(num1, num2)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   3,  5, 3)

    def test_2(self):
        test(self,   1,  12, 3)

    def test_3(self):
        test(self,   12,  1, 8)

    def test_4(self):
        test(self,   5,  3, 5)

if __name__ == '__main__':
    unittest.main()

'''

'''

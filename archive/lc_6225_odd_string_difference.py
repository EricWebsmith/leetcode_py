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


def get_pattern(s: str) -> int:
    ans = 0
    pre = ''
    for i, c in enumerate(s):
        if i == 0:
            pre = c
            continue
        v = 25 + ord(c) - ord(pre)
        ans = ans * 50
        ans += v
    return ans


class Solution:
    def oddString(self, words: List[str]) -> str:
        codes = []
        for i, word in enumerate(words):
            code = get_pattern(word)
            codes.append(code)
            if len(codes) == 3:
                if codes[0] == codes[1] and codes[1] == codes[2]:

                    continue
                elif codes[0] == codes[1]:
                    return words[2]
                elif codes[1] == codes[2]:
                    return words[0]
                elif codes[0] == codes[2]:
                    return words[1]
            elif len(codes) > 3:
                if code != codes[-2]:
                    return words[i]

        return words[-1]


def test(testObj: unittest.TestCase, words: List[str], expected: str) -> None:

    so = Solution()
    actual = so.oddString(words)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["adc", "wzy", "abc"], "abc")

    def test_2(self):
        test(self,   ["aaa", "bob", "ccc", "ddd"], "bob")

    def test_3(self):
        test(self,   ["abc", "wzy", "adc"], "abc")

    def test_4(self):
        test(self,   ["abc", "bcd", "def", "abb"], "abb")


if __name__ == '__main__':
    unittest.main()

'''

'''

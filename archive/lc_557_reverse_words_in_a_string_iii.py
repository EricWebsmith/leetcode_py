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
    def reverseWords(self, s: str) -> str:
        return ' '.join(t[::-1] for t in s.split(' '))


def test(testObj: unittest.TestCase, s: str, expected: str) -> None:

    so = Solution()

    actual = so.reverseWords(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "Let's take LeetCode contest",
             "s'teL ekat edoCteeL tsetnoc")

    def test_2(self):
        test(self,   "God Ding", "doG gniD")


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 53 ms, faster than 73.28% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.6 MB, less than 46.10% of Python3 online submissions for Reverse Words in a String III.
'''

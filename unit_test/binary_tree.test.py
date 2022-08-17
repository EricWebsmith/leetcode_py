import numpy

from curses import noecho
from heapq import heappop, heappush
import unittest
from typing import List, Optional
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from binary_tree import TreeNode, array_to_treenode, treenode_to_array


def test(testObj: unittest.TestCase, nums: List[int]) -> None:
    root = array_to_treenode(nums)
    actual = treenode_to_array(root)

    testObj.assertEqual(actual, nums)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  [1, 2, 3, 4, 5])

    def test_2(self):
        test(self,  [1, None, 2])

    def test_3(self):
        test(self,  [1, 2, 2, 3, 4, 4, 3])

    def test_4(self):
        test(self,  [1, 2, 2, None, 3, None, 3])


if __name__ == '__main__':
    unittest.main()

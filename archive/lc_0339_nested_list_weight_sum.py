
import os
import sys
import unittest
from typing import List

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def depthSum(self, nestedList: List[NestedInteger], depth: int = 1) -> int:
        ans = 0
        for i in nestedList:
            if i.isInteger():
                ans += depth * i.getInteger()
            else:
                ans += self.depthSum(i.getList(), depth+1)

        return ans


def test(testObj: unittest.TestCase, nestedList: List[NestedInteger], expected: int) -> None:

    s = Solution()
    actual = s.depthSum(nestedList)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  [[1, 1], 2, [1, 1]], 10)

    def test_2(self):
        test(self,  [1, [4, [6]]], 27)

    def test_3(self):
        test(self,  [0], 0)


if __name__ == '__main__':
    unittest.main()

"""
Runtime: 36 ms, faster than 86.00%
Memory Usage: 14.1 MB, less than 92.53%
"""

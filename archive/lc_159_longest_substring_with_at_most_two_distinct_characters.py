from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from queue import Queue
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        c1 = s[0]

        left = 0
        right = 0
        while right < n and s[right] == c1:
            right += 1

        if right == n:
            return n

        c2 = s[right]

        d = {}
        d[c1] = right - 1
        d[c2] = right

        max_length = 2
        while right < n:
            if not s[right] in [c1, c2]:
                # remove all c2 or c1
                if s[right-1] == c1:
                    left = d[c2] + 1
                    c2 = s[right]
                else:
                    left = d[c1] + 1
                    c1 = s[right]
            max_length = max(max_length, right-left+1)
            d[s[right]] = right
            right += 1

        return max_length


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()
    actual = so.lengthOfLongestSubstringTwoDistinct(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "eceba", 3)

    def test_2(self):
        test(self,   "ccaabbb", 5)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 298 ms, faster than 97.97% of Python3 online submissions for Longest Substring with At Most Two Distinct Characters.
Memory Usage: 14.8 MB, less than 38.02% of Python3 online submissions for Longest Substring with At Most Two Distinct Characters.
'''

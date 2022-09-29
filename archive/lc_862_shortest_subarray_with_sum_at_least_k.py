from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from collections import deque
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pres = [0] * (n + 1)

        for i in range(n):
            pres[i+1] = nums[i] + pres[i]

        ans = 1_000_000
        monoq = deque()

        for i, pre in enumerate(pres):
            while monoq and pre <= pres[monoq[-1]]:
                monoq.pop()

            while monoq and pre - pres[monoq[0]] >= k:
                ans = min(ans, i - monoq.popleft())

            monoq.append(i)

        return -1 if ans == 1_000_000 else ans


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: int) -> None:

    so = Solution()

    actual = so.shortestSubarray(nums, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1],  1, 1)

    def test_2(self):
        test(self,   [1, 2],  4, -1)

    def test_3(self):
        test(self,   [2, -1, 2],  3, 3)

    def test_4(self):
        test(self,   [0],  1, -1)

    def test_5(self):
        test(self,   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  5, 5)

    def test_6(self):
        test(self,   [84, -37, 32, 40, 95], 167,  3)

    def test_7(self):
        test(self,   [84, -37, 32, 40, 95, -100], 167,  3)

    def test_8(self):
        test(self,   [1, 1, 1, 1, 1, -3, 2, 2], 4,  2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1406 ms, faster than 88.70% of Python3 online submissions for Shortest Subarray with Sum at Least K.
Memory Usage: 28.3 MB, less than 73.12% of Python3 online submissions for Shortest Subarray with Sum at Least K.
'''

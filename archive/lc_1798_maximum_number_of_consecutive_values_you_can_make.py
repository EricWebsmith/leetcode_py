from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        cur_max = 0
        for coin in coins:
            if coin == 1:
                cur_max += coin
            elif coin <= cur_max + 1:
                cur_max += coin
            else:
                break

        return cur_max + 1


def test(testObj: unittest.TestCase, coins: List[int], expected: int) -> None:

    so = Solution()
    actual = so.getMaximumConsecutive(coins)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3], 2)

    def test_2(self):
        test(self,   [1, 1, 1, 4], 8)

    def test_3(self):
        test(self,   [1, 4, 10, 3, 1], 20)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 843 ms, faster than 89.76% of Python3 online submissions for Maximum Number of Consecutive Values You Can Make.
Memory Usage: 19.7 MB, less than 38.58% of Python3 online submissions for Maximum Number of Consecutive Values You Can Make.
'''

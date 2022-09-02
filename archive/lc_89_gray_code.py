from heapq import heappop, heappush
import unittest
from typing import List, Optional
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        prev = self.grayCode(n-1)
        ans = [i for i in prev]
        prev.reverse()
        ans += [i + 2 ** (n-1) for i in prev]

        return ans


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()
    actual = so.grayCode(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   2, [0, 1, 3, 2])

    def test_2(self):
        test(self,   1, [0, 1])

    def test_3(self):
        test(self,   3, [0, 1, 3, 2, 6, 7, 5, 4])

    def test_4(self):
        test(self,   4, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 197 ms, faster than 39.20% of Python3 online submissions for Gray Code.
Memory Usage: 21.5 MB, less than 31.80% of Python3 online submissions for Gray Code.
'''

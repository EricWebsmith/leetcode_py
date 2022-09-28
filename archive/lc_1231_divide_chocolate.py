import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def get_cuts(m):
            cuts = 0
            cur_sum = 0
            for s in sweetness:
                cur_sum += s
                if cur_sum >= m:
                    cuts += 1
                    cur_sum = 0

            return cuts

        left = 1
        right = sum(sweetness)

        while left < right:
            mid = left + (right - left + 1) // 2
            cuts = get_cuts(mid)
            if cuts >= k + 1:
                left = mid
            else:
                right = mid - 1

        return left


def test(testObj: unittest.TestCase, sweetness: List[int], k: int, expected: int) -> None:

    so = Solution()
    actual = so.maximizeSweetness(sweetness, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 4, 5, 6, 7, 8, 9],  5, 6)

    def test_2(self):
        test(self,   [5, 6, 7, 8, 9, 1, 2, 3, 4],  8, 1)

    def test_3(self):
        test(self,   [1, 2, 2, 1, 2, 2, 1, 2, 2],  2, 5)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 286 ms, faster than 74.81% of Python3 online submissions for Divide Chocolate.
Memory Usage: 15.3 MB, less than 60.19% of Python3 online submissions for Divide Chocolate.
'''

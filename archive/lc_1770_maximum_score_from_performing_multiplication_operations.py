import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)

        dp = [[0] * (m+1) for i in range(m+1)]

        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n-1-(i - left)
                dp[i][left] = max(mult * nums[left] + dp[i+1][left+1],
                                  mult * nums[right] + dp[i+1][left])

        return dp[0][0]


def test(testObj: unittest.TestCase, nums: List[int], multipliers: List[int], expected: int) -> None:

    so = Solution()

    actual = so.maximumScore(nums, multipliers)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3],  [3, 2, 1], 14)

    def test_2(self):
        test(self,   [-5, -3, -3, -2, 7, 1],  [-10, -5, 3, 4, 6], 102)

    def test_3(self):
        test(self,   [-1, 5, 7, 3, 9, 19], [-6, 9, 0, 8, 5], 284)

    def test_4(self):
        test(self,   [-1000], [-1000], 1_000_000)

    def test_5(self):
        test(self,   [1000], [-1000], -1_000_000)

    def test_6(self):
        test(self,   [-1000, 1000], [1000, -1000], 2_000_000)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 3997 ms, faster than 99.46% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
Memory Usage: 41.3 MB, less than 28.85% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
'''

# but the same can be Time Limit Exceeded

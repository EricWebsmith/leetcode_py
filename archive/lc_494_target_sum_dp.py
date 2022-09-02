from heapq import heappop, heappush
import unittest
from typing import List, Optional
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if abs(target) > total:
            return 0
        dp = [0] * (2 * total + 1)
        dp[total + nums[0]] += 1
        dp[total - nums[0]] += 1

        for i in range(1, n):
            next = [0] * (2 * total + 1)
            for s in range(-total, total+1):
                if dp[s+total] > 0:
                    next[total+s+nums[i]] += dp[s+total]
                    next[total+s-nums[i]] += dp[s+total]
            dp = next

        return dp[total + target]


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected: int) -> None:

    so = Solution()
    actual = so.findTargetSumWays(nums, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 1, 1, 1, 1],  3, 5)

    def test_2(self):
        test(self,   [1],  1, 1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 294 ms, faster than 81.18% of Python3 online submissions for Target Sum.
Memory Usage: 14 MB, less than 92.69% of Python3 online submissions for Target Sum.
'''

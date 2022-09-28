import unittest
from functools import cache
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        def dfs(n, target):
            MOD = 1_000_000_007
            if target <= 0:
                return 0
            if k * n < target:
                return 0
            if k * n == target:
                return 1
            if n == 1 and target <= k:
                return 1

            ans = 0
            for dice in range(1, k+1):
                ans += self.numRollsToTarget(n-1, k, target-dice)

            ans %= MOD

            return ans

        return dfs(n, target)


def test(testObj: unittest.TestCase, n: int, k: int, target: int, expected: int) -> None:
    so = Solution()
    actual = so.numRollsToTarget(n, k, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   1,  6,  3, 1)

    def test_2(self):
        test(self,   2,  6,  7, 6)

    def test_3(self):
        test(self,   30,  30,  500, 222616187)

    def test_4(self):
        test(self,   3,  6,  9, 25)

    def test_5(self):
        test(self,   2,  6,  5, 4)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 258 ms, faster than 89.74% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 18.3 MB, less than 42.91% of Python3 online submissions for Number of Dice Rolls With Target Sum.
'''

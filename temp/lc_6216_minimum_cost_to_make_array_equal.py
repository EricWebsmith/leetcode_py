import unittest
from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        last_num = 0
        total = 0
        left_unit_cost = 0
        right_unit_cost = 0

        for num, c in zip(nums, cost):
            total += num * c
            right_unit_cost += c

        best = total

        for num, c in sorted(zip(nums, cost)):
            distance = num - last_num

            total -= right_unit_cost * distance
            total += left_unit_cost * distance

            best = min(best, total)

            right_unit_cost -= c
            left_unit_cost += c
            last_num = num

        return best


def test(testObj: unittest.TestCase, nums: List[int], cost: List[int], expected: int) -> None:
    so = Solution()
    actual = so.minCost(nums, cost)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3, 5, 2],  [2, 3, 1, 14], 8)

    def test_2(self):
        test(self,   [2, 2, 2, 2, 2],  [4, 2, 8, 1, 3], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
2688 ms
Beats
46.15%
'''

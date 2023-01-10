import unittest
from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        n = len(nums)
        nums.sort()
        d: dict = dict()
        max_destroy = 0
        ans = 0
        for i in range(n-1, -1, -1):
            key = nums[i] % space
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
            if d[key] >= max_destroy:
                max_destroy = d[key]
                ans = nums[i]
        return ans


def test(testObj: unittest.TestCase, nums: List[int], space: int, expected: int) -> None:
    so = Solution()
    actual = so.destroyTargets(nums, space)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 7, 8, 1, 1, 5],  2, 1)

    def test_2(self):
        test(self,   [1, 3, 5, 2, 4, 6],  2, 1)

    def test_3(self):
        test(self,   [6, 2, 5],  100, 2)

    def test_4(self):
        test(self,   [1, 5, 3, 2, 2], 10000, 2)

    def test_5(self):
        test(self,   [2, 4, 6, 1, 1, 5],  2, 1)


if __name__ == '__main__':
    unittest.main()

'''

'''

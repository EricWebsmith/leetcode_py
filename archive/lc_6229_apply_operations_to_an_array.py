import unittest
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        ans = [0] * n
        ans_index = 0
        for i in range(n):
            if nums[i] != 0:
                ans[ans_index] = nums[i]
                ans_index += 1

        return ans


def test(testObj: unittest.TestCase, nums: List[int], expected: List[int]) -> None:

    so = Solution()

    actual = so.applyOperations(nums)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0])

    def test_2(self):
        test(self,   [0, 1], [1, 0])


if __name__ == '__main__':
    unittest.main()

'''

'''

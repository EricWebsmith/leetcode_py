import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # find pivot
        pivot = 0
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i
                break

        if pivot == 0:
            nums.reverse()
            return

        # then find the swap which first number > pivot
        swap = n - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1
        # swap
        nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
        nums[pivot:] = reversed(nums[pivot:])

        # reverse from pivot


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:

    so = Solution()
    so.nextPermutation(nums)
    testObj.assertEqual(nums, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3], [1, 3, 2])

    def test_2(self):
        test(self,   [3, 2, 1], [1, 2, 3])

    def test_3(self):
        test(self,   [1, 1, 5], [1, 5, 1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 39 ms, faster than 97.89%
Memory Usage: 13.9 MB, less than 24.98%
'''

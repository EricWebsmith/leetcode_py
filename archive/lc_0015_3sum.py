import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], i: int, result: List[List[int]]) -> None:
        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = nums[j] + nums[k]
            if s == -nums[i]:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1
            elif s > -nums[i]:
                k -= 1
            else:
                j += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: list[list[int]] = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, result)

        return result


def test(
    testObj: unittest.TestCase, nums: List[int], expected: List[List[int]]
) -> None:
    so = Solution()
    actual = so.threeSum(nums)
    actual.sort()
    expected.sort()
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])

    def test_2(self):
        test(self, [0, 1, 1], [])

    def test_3(self):
        test(self, [0, 0, 0], [[0, 0, 0]])

    def test_4(self):
        test(self, [0, 0, 0, 0], [[0, 0, 0]])

    def test_5(self):
        test(
            self,
            [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1909 ms
Beats
50.79%
"""

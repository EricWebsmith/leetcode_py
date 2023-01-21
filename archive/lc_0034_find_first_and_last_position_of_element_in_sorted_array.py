import unittest
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left = bisect_left(nums, target)
        # print(left)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect_right(nums, target) - 1
        return [left, right]


def test(
    testObj: unittest.TestCase, cardPoints: List[int], k: int, expected: int
) -> None:
    s = Solution()
    actual = s.searchRange(cardPoints, k)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [5, 7, 7, 8, 8, 10], 8, [3, 4])

    def test_2(self):
        test(self, [5, 7, 7, 8, 8, 10], 6, [-1, -1])

    def test_3(self):
        test(self, [], 0, [-1, -1])


if __name__ == "__main__":
    unittest.main()


# Runtime: 83 ms, faster than 98.27%
# Memory Usage: 15.4 MB, less than 92.49%

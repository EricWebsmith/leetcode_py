import unittest
from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        nums.sort(key=lambda x: (x & 1, x))
        target.sort(key=lambda x: (x & 1, x))
        ans = 0
        for i in range(n):
            diff = nums[i] - target[i]
            if diff > 0:
                ans += diff // 2

        return ans


def test(
    testObj: unittest.TestCase, nums: List[int], target: List[int], expected: int
) -> None:

    so = Solution()

    actual = so.makeSimilar(nums, target)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [8, 12, 6], [2, 14, 10], 2)

    def test_2(self):
        test(self, [1, 2, 5], [4, 1, 3], 1)

    def test_3(self):
        test(self, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 0)


if __name__ == "__main__":
    unittest.main()

"""

"""

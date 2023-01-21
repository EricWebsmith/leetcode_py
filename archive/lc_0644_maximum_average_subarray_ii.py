import unittest
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val, min_val, error = max(nums) * 1.0, min(nums) * 1.0, float("inf")
        prev_mid = max_val
        while error > 0.00001:
            mid = (max_val + min_val) / 2
            if self.check(nums, mid, k):
                min_val = mid
            else:
                max_val = mid
            error = abs(prev_mid - mid)
            prev_mid = mid
        return min_val

    def check(self, nums, mid, k):
        prev, min_sum = 0, 0
        total = sum([nums[i] - mid for i in range(k)])
        if total >= 0:
            return True
        for i in range(k, len(nums)):
            total += nums[i] - mid
            prev += nums[i - k] - mid
            min_sum = min(min_sum, prev)
            if total > min_sum:
                return True
        return False


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: float) -> None:
    so = Solution()
    actual = so.findMaxAverage(nums, k)
    testObj.assertTrue(abs(actual - expected) < 0.05)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 12, -5, -6, 50, 3], 4, 12.75000)

    def test_2(self):
        test(self, [5], 1, 5.00000)


if __name__ == "__main__":
    unittest.main()

"""

"""

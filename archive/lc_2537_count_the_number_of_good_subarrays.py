import unittest
from collections import defaultdict


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)
        d: dict[int, int] = defaultdict(int)

        left = 0
        ans = 0
        pairs = 0

        for right, num in enumerate(nums):
            pairs += d[num]
            d[num] += 1

            while pairs >= k:
                ans += n - right
                d[nums[left]] -= 1
                pairs -= d[nums[left]]
                left += 1

        return ans


def test(testObj: unittest.TestCase, nums: list[int], k: int, expected: int) -> None:
    so = Solution()
    actual = so.countGood(nums, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 1, 1, 1, 1], 10, 1)

    def test_2(self):
        test(self, [3, 1, 4, 3, 2, 2, 4], 2, 4)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
746 ms
Beats
100%
"""

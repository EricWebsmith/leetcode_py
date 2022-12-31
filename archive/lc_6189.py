import unittest
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = max(nums)

        ans = 1
        current = 0
        for i in range(n):
            if nums[i] == max_value:
                current += 1
            else:
                ans = max(ans, current)
                current = 0
        ans = max(ans, current)
        return ans


def test(testObj: unittest.TestCase, nums: List[int], expected: int) -> None:
    s = Solution()
    actual = s.longestSubarray(nums)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self, [1, 2, 3, 3, 2, 2], 2)

    def test_2(self):
        test(self, [1, 2, 3, 4], 1)

    def test_3(self):
        test(self, [1, 2, 3, 4, 5], 1)

    def test_4(self):
        test(self, [1, 2, 3, 4, 4, 4, 3, 2, 1], 3)

    def test_5(self):
        test(self, [378034, 378034, 378034], 3)


if __name__ == '__main__':
    unittest.main()

# Runtime: 741 ms, faster than 91.08%
# Memory Usage: 20.2 MB, less than 29.29%

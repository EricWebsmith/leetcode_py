import unittest
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        ans = 0
        if n % 2 == 1:
            for num in nums1:
                ans ^= num

        if m % 2 == 1:
            for num in nums2:
                ans ^= num

        return ans


def test(testObj: unittest.TestCase, nums1: List[int], nums2: List[int], expected: int) -> None:
    so = Solution()
    actual = so.xorAllNums(nums1, nums2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [2, 1, 3], [10, 2, 5, 0], 13)

    def test_2(self):
        test(self, [1, 2], [3, 4], 0)


if __name__ == "__main__":
    unittest.main()

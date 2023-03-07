import unittest
from typing import List

from sortedcontainers import SortedList  # type: ignore


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums3 = []
        for num1, num2 in zip(nums1, nums2):
            nums3.append(num1 - num2)

        nums4 = SortedList()
        ans = 0
        for num in nums3:
            index = nums4.bisect_right(num + diff)
            ans += index
            nums4.add(num)

        return ans


def test(
    testObj: unittest.TestCase,
    nums1: List[int],
    nums2: List[int],
    diff: int,
    expected: int,
) -> None:
    so = Solution()
    actual = so.numberOfPairs(nums1, nums2, diff)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [3, 2, 5], [2, 2, 1], 1, 3)

    def test_2(self):
        test(self, [3, -1], [-2, 2], -1, 0)


if __name__ == "__main__":
    unittest.main()

"""
1293ms, 100%
"""

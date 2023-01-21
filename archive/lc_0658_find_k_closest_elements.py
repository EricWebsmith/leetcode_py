import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        right = bisect_left(arr, x)
        left = right - 1
        condidate = 0
        while condidate < k:
            if right == n or (left >= 0 and x - arr[left] <= arr[right] - x):
                left -= 1
            else:
                right += 1
            condidate += 1

        return arr[left + 1 : right]


def test(
    testObj: unittest.TestCase, arr: List[int], k: int, x: int, expected: List[int]
) -> None:
    so = Solution()
    actual = so.findClosestElements(arr, k, x)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4])

    def test_2(self):
        test(self, [1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4])

    def test_3(self):
        test(self, [1, 2, 3, 4, 5], 4, 6, [2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 288 ms, faster than 98.53%
Memory Usage: 15.6 MB, less than 45.71%
"""

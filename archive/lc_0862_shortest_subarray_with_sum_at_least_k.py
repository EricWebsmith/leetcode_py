import unittest
from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pres = [0] * (n + 1)

        for i in range(n):
            pres[i + 1] = nums[i] + pres[i]

        ans = 1_000_000
        monoq = deque[int]()

        for i, pre in enumerate(pres):
            while monoq and pre <= pres[monoq[-1]]:
                monoq.pop()

            while monoq and pre - pres[monoq[0]] >= k:
                ans = min(ans, i - monoq.popleft())

            monoq.append(i)

        return -1 if ans == 1_000_000 else ans


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: int) -> None:

    so = Solution()
    actual = so.shortestSubarray(nums, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1], 1, 1)

    def test_2(self):
        test(self, [1, 2], 4, -1)

    def test_3(self):
        test(self, [2, -1, 2], 3, 3)

    def test_4(self):
        test(self, [0], 1, -1)

    def test_5(self):
        test(self, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5, 5)

    def test_6(self):
        test(self, [84, -37, 32, 40, 95], 167, 3)

    def test_7(self):
        test(self, [84, -37, 32, 40, 95, -100], 167, 3)

    def test_8(self):
        test(self, [1, 1, 1, 1, 1, -3, 2, 2], 4, 2)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 1406 ms, faster than 88.70%
Memory Usage: 28.3 MB, less than 73.12%
"""

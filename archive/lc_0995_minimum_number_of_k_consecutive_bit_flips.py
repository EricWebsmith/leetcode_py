import unittest
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        flips = [False] * n
        current = 0
        for i in range(n):
            if flips[i]:
                current ^= 1

            if nums[i] ^ current == 0:
                ans += 1
                current ^= 1
                if i+k > n:
                    return -1
                if i+k < n:
                    flips[i+k] = True

        return ans


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: int) -> None:

    so = Solution()

    actual = so.minKBitFlips(nums, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [0, 1, 0],  1, 2)

    def test_2(self):
        test(self,   [1, 1, 0],  2, -1)

    def test_3(self):
        test(self,   [0, 0, 0, 1, 0, 1, 1, 0],  3, 3)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1171 ms, faster than 90.00%
Memory Usage: 17.1 MB, less than 92.50%
'''

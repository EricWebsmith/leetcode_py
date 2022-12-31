import unittest
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [0] * (m + 1)
        ans = 0
        for r in range(m):
            new_dp = [0] * (m + 1)
            for c in range(n):
                if nums1[r] == nums2[c]:
                    new_dp[c+1] = dp[c] + 1
                    ans = max(new_dp[c+1], ans)
            dp = new_dp

        return ans


def test(testObj: unittest.TestCase, nums1: List[int], nums2: List[int], expected: int) -> None:

    so = Solution()

    actual = so.findLength(nums1, nums2)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 2, 1],  [3, 2, 1, 4, 7], 3)

    def test_2(self):
        test(self,   [0, 0, 0, 0, 0],  [0, 0, 0, 0, 0], 5)

    def test_3(self):
        test(self,   [0, 1, 0, 0, 0],  [0, 0, 0, 0, 0], 3)

    def test_4(self):
        test(self,   [0, 1, 0, 0, 0],  [2, 3, 4], 0)

    def test_5(self):
        test(self,   [0, 0, 0, 0, 1], [1, 0, 0, 0, 0], 4)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 6260 ms, faster than 45.01%
Memory Usage: 13.8 MB, less than 99.96%
'''

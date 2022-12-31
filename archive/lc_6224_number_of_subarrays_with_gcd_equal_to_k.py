import unittest
from typing import List


def gcd(m, n):
    return gcd(abs(m-n), min(m, n)) if (m-n) else n


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            theGcd = nums[i]
            if theGcd == k:
                ans += 1
            elif theGcd < k:
                continue
            for j in range(i+1, n):
                theGcd = gcd(theGcd, nums[j])
                if theGcd == k:
                    ans += 1
                elif theGcd < k:
                    break

        return ans


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: int) -> None:

    so = Solution()

    actual = so.subarrayGCD(nums, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [9, 3, 1, 2, 6, 3],  3, 4)

    def test_2(self):
        test(self,   [4],  7, 0)

    def test_3(self):
        test(self,   [12, 9, 6, 2, 6, 3],  3, 5)


if __name__ == '__main__':
    unittest.main()

'''

'''

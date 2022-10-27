import unittest
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pres = [nums[0] % k]
        for i in range(1, n):
            pres.append((pres[i-1] + nums[i]) % k)

        s = set()
        previous = pres[0]
        for i in range(1, n):
            if pres[i] == 0:
                return True
            if pres[i] in s:
                return True
            s.add(previous)
            previous = pres[i]

        return False


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: bool) -> None:
    so = Solution()
    actual = so.checkSubarraySum(nums, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [23, 2, 4, 6, 7],  6, True)

    def test_2(self):
        test(self,   [23, 2, 6, 4, 7],  6, True)

    def test_3(self):
        test(self,   [23, 2, 6, 4, 7],  13, False)

    def test_4(self):
        test(self,   [1, 0],  2, False)


if __name__ == '__main__':
    unittest.main()

'''

'''

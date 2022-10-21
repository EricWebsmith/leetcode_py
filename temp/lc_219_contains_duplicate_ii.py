import unittest
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                prev = d[num]
                if i-prev <= k:
                    return True

            d[num] = i

        return False


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: bool) -> None:
    so = Solution()
    actual = so.containsNearbyDuplicate(nums, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 1],  3, True)

    def test_2(self):
        test(self,   [1, 0, 1, 1],  1, True)

    def test_3(self):
        test(self,   [1, 2, 3, 1, 2, 3],  2, False)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
669 ms
Beats
87.63%
'''

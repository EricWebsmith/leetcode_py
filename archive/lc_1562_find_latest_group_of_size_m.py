
import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        keys = []
        for i in range(n-1, -1, -1):
            index = bisect_left(keys, arr[i])
            keys.insert(index, arr[i])
            left = keys[index]-1 if index == 0 else keys[index] - keys[index-1] - 1
            right = n-keys[index] if index == len(keys)-1 else keys[index+1]-keys[index]-1
            if left == m or right == m:
                return i

        return -1


def test(testObj: unittest.TestCase, arr: List[int], m: int, expected: int) -> None:

    so = Solution()
    actual = so.findLatestStep(arr, m)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 5, 1, 2, 4],  1, 4)

    def test_2(self):
        test(self,   [3, 1, 5, 4, 2],  2, -1)


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 8240 ms, faster than 5.48%
Memory Usage: 28 MB, less than 93.29%
"""

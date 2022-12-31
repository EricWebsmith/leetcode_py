import unittest
from typing import List

MAX_INT = 2 ** 31 - 1


class ArrayReader:
    def __init__(self, arr) -> None:
        self.arr = arr

    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return MAX_INT
        return self.arr[index]


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        left = 0
        right = 10000
        while left < right:
            mid = (left + right) >> 1
            if reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid

        if reader.get(left) == target:
            return left

        return -1


def test(testObj: unittest.TestCase, arr: List[int], target: int, expected: int) -> None:

    reader = ArrayReader(arr)
    so = Solution()
    actual = so.search(reader, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [-1, 0, 3, 5, 9, 12],  9, 4)

    def test_2(self):
        test(self,   [-1, 0, 3, 5, 9, 12],  2, -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 47 ms, faster than 80.53%
Memory Usage: 15.1 MB, less than 55.25%
'''

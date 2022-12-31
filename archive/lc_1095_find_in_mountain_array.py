import unittest
from typing import List


class MountainArray:
    def __init__(self, arr) -> None:
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountain: 'MountainArray') -> int:
        n = mountain.length()

        left = 1
        right = n - 2
        mid = 0
        mid_value = 0
        while left < right:
            mid = (left + right + 1) >> 1
            mid_value = mountain.get(mid)
            if mid_value > target:
                break
            next_value = mountain.get(mid+1)
            if next_value > mid_value:
                left = mid + 1
            else:
                right = mid - 1

        # find target at left
        left = 0
        right = mid
        while left <= right:
            mid = (left + right + 1) >> 1
            mid_value = mountain.get(mid)
            if mid_value == target:
                break
            if mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        if mid_value == target:
            return mid

        # find target at right
        left = mid
        right = n - 1
        while left <= right:
            mid = (left + right + 1) >> 1
            mid_value = mountain.get(mid)
            if mid_value == target:
                break
            if mid_value < target:
                right = mid - 1
            else:
                left = mid + 1

        if mid_value == target:
            return mid

        return -1


def test(testObj: unittest.TestCase, arr: List[int], target: int, expected: int) -> None:
    mountain = MountainArray(arr)
    so = Solution()
    actual = so.findInMountainArray(target, mountain)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 4, 5, 3, 1],  3, 2)

    def test_2(self):
        test(self,   [0, 1, 2, 4, 2, 1],  3, -1)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 42 ms, faster than 70.92%
Memory Usage: 14.8 MB, less than 60.53%
'''

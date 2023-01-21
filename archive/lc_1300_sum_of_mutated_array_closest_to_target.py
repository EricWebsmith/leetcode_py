import unittest
from typing import List


class Solution:
    def get_sum(self, arr: List[int], threshold: int):
        sum = 0
        for i in range(len(arr)):
            if arr[i] >= threshold:
                sum += threshold
            else:
                sum += arr[i]
        return sum

    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = target // n - 1
        right = max(arr)

        while left < right:
            m = (left + right) // 2
            s = self.get_sum(arr, m)
            if s < target:
                left = m + 1
            else:
                right = m

        l_value = target - self.get_sum(arr, left - 1)
        r_value = self.get_sum(arr, left) - target
        if l_value <= r_value:
            return left - 1
        else:
            return left


def test(
    testObj: unittest.TestCase, arr: List[int], target: int, expected: int
) -> None:

    so = Solution()
    actual = so.findBestValue(arr, target)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [4, 9, 3], 10, 3)

    def test_2(self):
        test(self, [2, 3, 5], 10, 5)

    def test_3(self):
        test(self, [60864, 25176, 27249, 21296, 20204], 56803, 11361)


if __name__ == "__main__":
    unittest.main()

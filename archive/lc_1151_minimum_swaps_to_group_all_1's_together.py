import unittest
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        window_size = sum(data)

        count = sum(data[:window_size])
        max_count = count
        for i in range(window_size, n):
            if data[i - window_size] == 1:
                count -= 1
            if data[i] == 1:
                count += 1
            max_count = max(max_count, count)

        return window_size - max_count


def test(testObj: unittest.TestCase, data: List[int], expected: int) -> None:

    so = Solution()
    actual = so.minSwaps(data)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [1, 0, 1, 0, 1], 1)

    def test_2(self):
        test(self, [0, 0, 0, 1, 0], 0)

    def test_3(self):
        test(self, [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1], 3)


if __name__ == "__main__":
    unittest.main()


"""
Runtime: 995 ms, faster than 69.53%
Memory Usage: 18 MB, less than 14.82%
"""

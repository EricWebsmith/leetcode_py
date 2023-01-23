import unittest
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(growTime)
        arr = list(zip(growTime, plantTime))
        arr.sort()
        waste = arr[0][0]
        plant = arr[0][1]
        for i in range(1, n):
            waste = max(waste, arr[i][0] - plant)
            plant += arr[i][1]

        return sum(plantTime) + waste


def test(testObj: unittest.TestCase, plantTime: List[int], growTime: List[int], expected: int) -> None:

    so = Solution()
    actual = so.earliestFullBloom(plantTime, growTime)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 4, 3], [2, 3, 1], 9)

    def test_2(self):
        test(self, [1, 2, 3, 2], [2, 1, 2, 1], 9)

    def test_3(self):
        test(self, [1], [1], 2)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 1841 ms, faster than 88.99%
Memory Usage: 30.9 MB, less than 88.11%
"""

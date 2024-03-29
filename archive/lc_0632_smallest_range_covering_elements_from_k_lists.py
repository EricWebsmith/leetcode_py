import unittest
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)

        hq: list = []
        high = -100000
        for i in range(k):
            hq.append((nums[i][0], i, 0))
            high = max(high, nums[i][0])
        heapify(hq)
        result = [hq[0][0], high]

        while True:
            lo, arr_index, index = heappop(hq)
            if index == len(nums[arr_index]) - 1:
                break
            high = max(high, nums[arr_index][index + 1])
            heappush(hq, (nums[arr_index][index + 1], arr_index, index + 1))  # type: ignore

            if result[1] - result[0] > high - hq[0][0]:
                result = [hq[0][0], high]

        return result


def test(testObj: unittest.TestCase, nums: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.smallestRange(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24])

    def test_2(self):
        test(self, [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 1])


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 229 ms, faster than 97.97%
Memory Usage: 20.4 MB, less than 49.45%
"""

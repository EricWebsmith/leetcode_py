import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        acc = [nums[0]]
        for i in range(1, n):
            acc.append(acc[i - 1] + nums[i])

        ans: list = []
        for q in queries:
            index = bisect_right(acc, q)
            if index == 0:
                ans.append(0)
            else:
                ans.append(index)

        return ans


def test(
    testObj: unittest.TestCase, nums: List[int], queries: List[int], expected: int
) -> None:

    so = Solution()
    actual = so.answerQueries(nums, queries)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [4, 5, 2, 1], [3, 10, 21], [2, 3, 4])

    def test_2(self):
        test(self, [2, 3, 4, 5], [1], [0])

    def test_3(self):
        test(
            self,
            [469781, 45635, 628818, 324948, 343772, 713803, 452081],
            [816646, 929491],
            [3, 3],
        )


if __name__ == "__main__":
    unittest.main()

"""

"""

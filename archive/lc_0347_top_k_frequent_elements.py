import unittest
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        first_k = c.most_common(k)
        return [k for k, _ in first_k]


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected: List[int]) -> None:
    so = Solution()
    actual = so.topKFrequent(nums, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 1, 1, 2, 2, 3], 2, [1, 2])

    def test_2(self):
        test(self, [1], 1, [1])


if __name__ == "__main__":
    unittest.main()

"""
Runtime
181 ms
Beats
72.78%
"""

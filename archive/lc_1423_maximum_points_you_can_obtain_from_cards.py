import unittest
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)

        current = sum(cardPoints[:k])
        maxAns = current
        for i in range(0, k):
            current -= cardPoints[k - 1 - i]
            current += cardPoints[n - 1 - i]
            maxAns = max(maxAns, current)

        return maxAns


def test(
    testObj: unittest.TestCase, cardPoints: List[int], k: int, expected: int
) -> None:
    s = Solution()
    actual = s.maxScore(cardPoints, k)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5, 6, 1], 3, 12)

    def test_2(self):
        test(self, [2, 2, 2], 2, 4)

    def test_3(self):
        test(self, [9, 7, 7, 9, 7, 7, 9], 7, 55)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 461 ms, faster than 84.66%
Memory Usage: 27.4 MB, less than 40.17%
"""

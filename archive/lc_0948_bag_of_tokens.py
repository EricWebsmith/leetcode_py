import unittest
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        # edge case
        if n == 0:
            return 0
        tokens.sort()
        left = 0
        right = n - 1
        score = 0
        max_score = 0

        while left < right:
            if score == 0:
                # use power to gain score
                if power > tokens[left]:
                    power -= tokens[left]
                    left += 1
                    score += 1
                else:
                    break
            else:
                # use power to gain score
                if power > tokens[left]:
                    power -= tokens[left]
                    left += 1
                    score += 1
                else:
                    power += tokens[right]
                    right -= 1
                    score -= 1
            max_score = max(max_score, score)

        if power >= tokens[left]:
            score += 1
            max_score = max(max_score, score)

        return max_score


def test(testObj: unittest.TestCase, tokens: List[int], power: int, expected: int) -> None:

    so = Solution()

    actual = so.bagOfTokensScore(tokens, power)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [100], 50, 0)

    def test_2(self):
        test(self, [100, 200], 150, 1)

    def test_3(self):
        test(self, [100, 200, 300, 400], 200, 2)

    def test_4(self):
        test(self, [], 200, 0)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 51 ms, faster than 98.58%
Memory Usage: 14 MB, less than 77.36%
"""

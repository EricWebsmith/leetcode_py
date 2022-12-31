
import string
import unittest
from typing import List

import numpy as np


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = string.ascii_lowercase

        indices = [string.ascii_lowercase.index(ss) for ss in s]
        indices = np.array(indices)

        for start, end, direction in shifts:
            if direction == 0:
                indices[start: end+1] = indices[start: end+1] - 1

            else:
                indices[start: end+1] = indices[start: end+1] + 1

        ans = "".join([letters[i % 26] for i in indices])
        return ans


def test(testObj: unittest.TestCase, s: str, shifts: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.shiftingLetters(s, shifts)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  "abc",  [[0, 1, 0], [1, 2, 1], [0, 2, 1]], "ace")

    def test_2(self):
        test(self,  "dztz",  [[0, 0, 0], [1, 1, 1]], "catz")


if __name__ == '__main__':
    unittest.main()


"""
Runtime: 9256 ms, faster than 20.00%
Memory Usage: 57.3 MB, less than 40.00%
"""

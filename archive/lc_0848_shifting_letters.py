
import unittest
from typing import List


class Solution:
    def shiftingLetters(self, S, shifts) -> str:
        ans = []
        X = sum(shifts) % 26
        for i, c in enumerate(S):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26

        return "".join(ans)


def test(testObj: unittest.TestCase, s: str, shifts: List[int], expected: int) -> None:

    so = Solution()
    actual = so.shiftingLetters(s, shifts)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  "abc",  [3, 5, 9], "rpl")

    def test_2(self):
        test(self,  "aaa",  [1, 2, 3], "gfd")


if __name__ == '__main__':
    unittest.main()

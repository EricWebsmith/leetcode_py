import unittest
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        ans = [pref[0]]
        for i in range(1, n):
            ans.append(pref[i - 1] ^ 0 ^ pref[i])

        return ans


def test(testObj: unittest.TestCase, pref: List[int], expected: List[int]) -> None:
    so = Solution()
    actual = so.findArray(pref)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [5, 2, 0, 3, 1], [5, 7, 2, 3, 2])

    def test_2(self):
        test(self, [13], [13])


if __name__ == "__main__":
    unittest.main()

"""

"""

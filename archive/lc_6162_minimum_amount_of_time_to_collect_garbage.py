import unittest
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        last_m = -1
        last_p = -1
        last_g = -1
        picks = 0
        for i in range(n):
            if 'M' in garbage[i]:
                last_m = i
            if 'P' in garbage[i]:
                last_p = i
            if 'G' in garbage[i]:
                last_g = i
            picks += len(garbage[i])

        drive = 0
        s = 0
        for i in range(len(travel)+1):
            if last_m == i:
                drive += s
            if last_p == i:
                drive += s
            if last_g == i:
                drive += s
            if i < len(travel):
                s += travel[i]

        return picks + drive


def test(testObj: unittest.TestCase, garbage: List[str], travel: List[int], expected: int) -> None:

    so = Solution()
    actual = so.garbageCollection(garbage, travel)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["G", "P", "GP", "GG"],  [2, 4, 3], 21)

    def test_2(self):
        test(self,   ["MMM", "PGM", "GP"],  [3, 10], 37)


if __name__ == '__main__':
    unittest.main()

'''

'''

import unittest
from math import floor, sqrt
from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:

        ans: List[int] = []
        best_q = -1
        for x in range(0, 50+1):
            for y in range(0, 50+1):
                q = 0
                for tx, ty, tq in towers:
                    d = sqrt((tx-x)**2 + (ty-y)**2)
                    if d <= radius:
                        q += floor(tq / (1+d))

                if q > best_q:
                    best_q = q
                    ans = [x, y]

        return ans


def test(testObj: unittest.TestCase, towers: List[List[int]], radius: int, expected: List[int]) -> None:

    so = Solution()

    actual = so.bestCoordinate(towers, radius)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[1, 2, 5], [2, 1, 7], [3, 1, 9]],  2, [2, 1])

    def test_2(self):
        test(self,   [[23, 11, 21]],  9, [23, 11])

    def test_3(self):
        test(self,   [[1, 2, 13], [2, 1, 7], [0, 1, 9]],  2, [1, 2])

    def test_4(self):
        test(self,   [[42, 0, 0]],  7, [0, 0])

    def test_5(self):
        test(self,   [[50, 20, 31], [43, 36, 29]],  38, [50, 20])

    def test_6(self):
        test(self,   [[0, 1, 2], [2, 1, 2], [1, 0, 2], [1, 2, 2]],  1, [1, 1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime
2284 ms
Beats
64.96%
'''

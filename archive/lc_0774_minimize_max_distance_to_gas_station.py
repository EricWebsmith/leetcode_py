import unittest
from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(D):
            return sum(int((stations[i + 1] - stations[i]) / D) for i in range(len(stations) - 1)) <= k

        lo, hi = 0.0, 10**8 + 0.0
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo


def test(testObj: unittest.TestCase, stations: List[int], k: int, expected: float) -> None:

    so = Solution()

    actual = so.minmaxGasDist(stations, k)
    print(actual, expected)
    testObj.assertAlmostEqual(actual, expected, 5)
    # testObj.assertTrue(abs(actual-expected) < 0.000001)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9, 0.50000)

    def test_2(self):
        test(self, [23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1, 14.00000)

    def test_3(self):
        test(self, [10, 19, 25, 27, 56, 63, 70, 87, 96, 97], 3, 9.66667)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 668 ms, faster than 48.34%
Memory Usage: 14.2 MB, less than 79.38%
"""

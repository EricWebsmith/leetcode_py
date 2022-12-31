
import unittest
from heapq import heappop, heappush
from typing import List


class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)
        max_in_lo = -heappop(self.lo)
        heappush(self.hi, max_in_lo)

        if len(self.lo) < len(self.hi):
            min_in_hi = -heappop(self.hi)
            heappush(self.lo, min_in_hi)

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0])/2.0
        else:
            return -self.lo[0]


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = MedianFinder(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:
            case "addNum":
                actual = obj.addNum(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "findMedian":
                actual = obj.findMedian(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [
             [], [1], [2], [], [3], []], [None, None, None, 1.5, None, 2.0])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 568 ms, faster than 93.03%
Memory Usage: 36.4 MB, less than 21.94%
'''

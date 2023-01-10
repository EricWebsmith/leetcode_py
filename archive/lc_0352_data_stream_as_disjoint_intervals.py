import unittest
from bisect import bisect_left
from typing import List


class SummaryRanges:

    def __init__(self) -> None:
        self.intervals: list = []

    def addNum(self, val: int) -> None:
        if len(self.intervals) == 0:
            self.intervals.append([val, val])
            return

        insert_pos = bisect_left(self.intervals, val, key=lambda x: x[0])
        # merge left and right
        if insert_pos > 0 and insert_pos < len(self.intervals) \
                and self.intervals[insert_pos-1][1] - val >= -1 \
                and self.intervals[insert_pos][0] - val <= 1:
            self.intervals = self.intervals[0:insert_pos - 1] \
                + [[self.intervals[insert_pos-1][0], self.intervals[insert_pos][1]]] + \
                self.intervals[insert_pos+1:]
        elif insert_pos > 0 \
                and self.intervals[insert_pos-1][1] - val >= -1:
            self.intervals = self.intervals[0:insert_pos - 1] \
                + [[self.intervals[insert_pos-1][0], max(self.intervals[insert_pos-1][1], val)]] + \
                self.intervals[insert_pos:]
        elif insert_pos < len(self.intervals) \
                and self.intervals[insert_pos][0] - val <= 1:
            self.intervals = self.intervals[0:insert_pos] \
                + [[val, self.intervals[insert_pos][1]]] + \
                self.intervals[insert_pos+1:]
        else:
            self.intervals = self.intervals[0:insert_pos] \
                + [[val, val]] + \
                self.intervals[insert_pos:]

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = SummaryRanges(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "addNum":
                obj.addNum(*params[i])

            case "getIntervals":
                actual = obj.getIntervals(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
                    "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"],
             [[], [1], [], [3], [], [7], [], [2], [], [6], []],
             [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None,
             [[1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]], None, [[1, 3], [6, 7]]])

    def test_2(self):
        test(self,
             ["SummaryRanges", "addNum", "getIntervals", "addNum",
                 "getIntervals", "addNum", "getIntervals"],
             [[], [1], [], [9], [], [2], []],
             [None, None, [[1, 1]], None, [[1, 1], [9, 9]], None, [[1, 2], [9, 9]]])

    def test_3(self):
        test(self,
             ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals",
              "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
              "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"],
             [[], [6], [], [6], [], [0], [], [4], [], [8], [],
                 [7], [], [6], [], [4], [], [7], [], [5], []],
             [None, None, [[6, 6]], None, [[6, 6]], None, [[0, 0], [6, 6]], None,
              [[0, 0], [4, 4], [6, 6]], None,
              [[0, 0], [4, 4], [6, 6], [8, 8]], None, [[0, 0], [4, 4], [6, 8]], None,
              [[0, 0], [4, 4], [6, 8]], None, [[0, 0], [4, 4], [6, 8]], None,
              [[0, 0], [4, 4], [6, 8]], None, [[0, 0], [4, 8]]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 325 ms, faster than 35.25%
Memory Usage: 19 MB, less than 48.30%
'''

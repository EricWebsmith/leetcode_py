import unittest
from bisect import bisect_left, bisect_right
from typing import List


class RangeModule:

    def __init__(self):
        self.arr = []

    def addRange(self, left: int, right: int) -> None:
        # Main Logic
        #   If idx(left) or idx(right) is odd, it's in a interval. So don't add it.
        #   If idx(left) or idx(right) is even, it's not in any interval. So add it as new interval
        #   Slice array[idx(left) : idx(right)]
        #       1) both odd: Nothing is added. Merge all middle intervals.
        #       2) both even: Add new intervals. Merge all middle intervals
        #       3) idx(left) is even: update start point of next interval with left
        #       4) idx(right) is even: update end point of previous interval with right
        # Bisect_left vs. Bisect_right
        #   left need to proceed all interval closing at left, so use Bisect_left
        #   right need to go after all interval openning at right, so use Bisect_right
        i, j = bisect_left(self.arr, left), bisect_right(self.arr, right)
        self.arr[i: j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        # Main logic
        #   If idx of left/right is odd, it's in a interval. Else it's not.
        #   If idx of left&right is the same, they're in the same interval
        # Bisect_left vs. Bisect_right
        #   [start, end). Start is included. End is not.
        #   so use bisect_right for left
        #   so use bisect_left for right
        i, j = bisect_right(self.arr, left), bisect_left(self.arr, right)
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        # Main Logic
        #   If idx(left) is odd, the interval that contains left need to change end point to left
        #   If idx(right) is odd, the interval that contains right need to change start point to right
        #   Else, everything from idx(left) to idx(right) is removed. Nothing is changed.
        # Bisect_left vs. Bisect_right
        #   Same as addRange
        i, j = bisect_left(self.arr, left), bisect_right(self.arr, right)
        self.arr[i: j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = RangeModule(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "addRange":
                obj.addRange(*params[i])

            case "queryRange":
                actual = obj.queryRange(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "removeRange":
                obj.removeRange(*params[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"], [
             [], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]], [None, None, None, True, False, True])

    def test_2(self):
        test(self, ["RangeModule", "addRange", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"], [
             [], [10, 20], [30, 40], [15, 35], [10, 14], [13, 15], [16, 17]],
             [None, None, None, None, True, True, False])

    def test_3(self):
        test(self, ["RangeModule", "addRange", "removeRange", "removeRange",
                    "addRange", "removeRange", "addRange", "queryRange", "queryRange", "queryRange"],
             [[], [6, 8], [7, 8], [8, 9], [8, 9], [1, 3], [1, 8], [2, 4], [2, 9], [4, 6]],
             [None, None, None, None, None, None, None, True, True, True])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 384 ms, faster than 95.08%
Memory Usage: 18.6 MB, less than 61.51%
'''

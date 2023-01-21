import unittest
from bisect import bisect_left, insort_left, insort_right
from typing import List


class ExamRoom:
    def __init__(self, n: int) -> None:
        self.n = n
        self.occupied: list = []
        self.gaps: list = []
        self.gap_key = lambda x: x[0] * 1_000_000_000 - x[1]

    def gap_func(self, left, right):
        return (right - left - 2) // 2

    # in insort_right, x is tuple
    def _insert_gap(self, left: int, right: int):
        x = (self.gap_func(left, right), left, right)
        insort_right(self.gaps, x=x, key=self.gap_key)

    # in bisect_left, x is not tuple, x is int
    def _find_gap(self, left: int, right: int) -> int:
        x = (self.gap_func(left, right), left, right)
        key = self.gap_key(x)
        return bisect_left(self.gaps, x=key, key=self.gap_key)

    def seat(self) -> int:
        n = self.n
        occupied = self.occupied
        gaps = self.gaps
        if not self.occupied:
            self.occupied.append(0)
            return 0
        # from seat 0 to the first occupied seat
        first_dis = occupied[0] - 1
        # from Seat n-1 to the last occupied seat
        last_dis = n - 1 - occupied[-1] - 1
        mid_dis = gaps[-1][0] if gaps else -1
        max_dis = max([first_dis, last_dis, mid_dis])
        if first_dis == max_dis:
            self._insert_gap(0, occupied[0])
            occupied.insert(0, 0)
            return 0
        elif mid_dis == max_dis:
            _, left, right = gaps.pop()
            seat = (left + right) >> 1
            self._insert_gap(left, seat)
            self._insert_gap(seat, right)
            insort_left(occupied, seat)
            return seat
        else:
            self._insert_gap(occupied[-1], n - 1)
            occupied.append(n - 1)
            return n - 1

    def leave(self, p: int) -> None:
        occupied = self.occupied
        if len(occupied) == 1:
            self.occupied = []
            self.gaps = []
            return
        gaps = self.gaps
        p_at = bisect_left(occupied, p)
        gap_removes: list = []
        if p_at < len(occupied) - 1:
            left_gap_index = self._find_gap(occupied[p_at], occupied[p_at + 1])
            gap_removes.append(left_gap_index)
        if p_at > 0:
            right_gap_index = self._find_gap(occupied[p_at - 1], occupied[p_at])
            gap_removes.append(right_gap_index)
        gap_removes.sort()
        while gap_removes:
            del gaps[gap_removes.pop()]

        if 0 < p_at < len(occupied) - 1:
            self._insert_gap(occupied[p_at - 1], occupied[p_at + 1])

        del self.occupied[p_at]


def test(
    testObj: unittest.TestCase, actions: List, params: List, expected: List
) -> None:
    n = len(actions)
    obj = ExamRoom(*params[0])
    print("------------test case-----------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print("-------done-------------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "seat":
                actual = obj.seat(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "leave":
                obj.leave(*params[i])
                testObj.assertEqual(None, expected[i])


class TestClass(unittest.TestCase):
    def test_10(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[10], [], [], [], [], [4], []],
            [None, 0, 9, 4, 2, None, 5],
        )

    def test_100_0(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[100], [], [], [], [], [0], []],
            [None, 0, 99, 49, 74, None, 0],
        )

    def test_100_49(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[100], [], [], [], [], [49], []],
            [None, 0, 99, 49, 74, None, 37],
        )

    def test_100_74(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[100], [], [], [], [], [74], []],
            [None, 0, 99, 49, 74, None, 74],
        )

    def test_100_99(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[100], [], [], [], [], [99], []],
            [None, 0, 99, 49, 74, None, 99],
        )

    def test_1000(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[1000], [], [], [], [], [749], []],
            [None, 0, 999, 499, 749, None, 749],
        )

    def test_10000(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[10000], [], [], [], [], [7499], []],
            [None, 0, 9999, 4999, 7499, None, 7499],
        )

    def test_50000(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[50000], [], [], [], [], [37499], []],
            [None, 0, 49999, 24999, 37499, None, 37499],
        )

    def test_1000000000(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
            [[1000000000], [], [], [], [], [749999999], []],
            [None, 0, 999999999, 499999999, 749999999, None, 749999999],
        )

    def test_4(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "leave", "seat"],
            [[4], [], [], [], [], [1], [3], []],
            [None, 0, 3, 1, 2, None, None, 1],
        )

    def test_2(self):
        test(
            self,
            ["ExamRoom", "seat", "seat", "leave"],
            [[2], [], [], [0]],
            [None, 0, 1, None],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 174 ms, faster than 66.45%
Memory Usage: 18.1 MB, less than 52.99%
"""

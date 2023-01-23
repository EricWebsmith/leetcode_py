import unittest
from typing import List


def to_minute(s: str):
    h, m = s.split(":")
    minute = int(h) * 60 + int(m)
    return minute


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1 = [to_minute(event1[0]), to_minute(event1[1])]
        e2 = [to_minute(event2[0]), to_minute(event2[1])]
        time1 = e1[1] - e1[0]
        time2 = e2[1] - e2[0]
        time_all = max(e1[1], e2[1]) - min(e1[0], e2[0])
        return time_all <= time1 + time2


def test(testObj: unittest.TestCase, event1: List[str], event2: List[str], expected: bool) -> None:

    so = Solution()

    actual = so.haveConflict(event1, event2)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, ["01:15", "02:00"], ["02:00", "03:00"], True)

    def test_2(self):
        test(self, ["01:00", "02:00"], ["01:20", "03:00"], True)

    def test_3(self):
        test(self, ["10:00", "11:00"], ["14:00", "15:00"], False)


if __name__ == "__main__":
    unittest.main()

"""

"""

import unittest
from bisect import bisect_right
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TimedValue:
    times: List[int]
    values: List[str]


class TimeMap:
    def __init__(self) -> None:
        self.d: Dict[str, TimedValue] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = TimedValue([], [])
        tv = self.d[key]
        tv.times.append(timestamp)
        tv.values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        tv = self.d[key]
        if timestamp < tv.times[0]:
            return ""

        index = bisect_right(tv.times, timestamp, 0, len(tv.times))
        return tv.values[index - 1]


def test(
    testObj: unittest.TestCase, actions: List, params: List, expected: List
) -> None:
    n = len(actions)
    obj = TimeMap()
    for i in range(1, n):
        match actions[i]:
            case "set":
                obj.set(*params[i])

            case "get":
                actual = obj.get(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(
            self,
            ["TimeMap", "set", "get", "get", "set", "get", "get"],
            [
                [],
                ["foo", "bar", 1],
                ["foo", 1],
                ["foo", 3],
                ["foo", "bar2", 4],
                ["foo", 4],
                ["foo", 5],
            ],
            [None, None, "bar", "bar", None, "bar2", "bar2"],
        )

    def test_2(self):
        test(
            self,
            ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
            [
                [],
                ["love", "high", 10],
                ["love", "low", 20],
                ["love", 5],
                ["love", 10],
                ["love", 15],
                ["love", 20],
                ["love", 25],
            ],
            [None, None, None, "", "high", "high", "low", "low"],
        )

    def test_3(self):
        test(
            self,
            ["TimeMap", "set", "set", "get", "set", "get", "get"],
            [
                [],
                ["a", "bar", 1],
                ["x", "b", 3],
                ["b", 3],
                ["foo", "bar2", 4],
                ["foo", 4],
                ["foo", 5],
            ],
            [None, None, None, "", None, "bar2", "bar2"],
        )


if __name__ == "__main__":
    unittest.main()


"""
Runtime: 827 ms, faster than 85.22%
Memory Usage: 69.8 MB, less than 92.60%
"""

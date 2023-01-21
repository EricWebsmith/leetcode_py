import random
import unittest
from bisect import bisect_left
from typing import List


class RandomizedCollection:
    def __init__(self) -> None:
        self.arr: list = []

    def insert(self, val: int) -> bool:
        index = bisect_left(self.arr, val)
        ans = not (index < len(self.arr) and self.arr[index] == val)
        self.arr.insert(index, val)
        return ans

    def remove(self, val: int) -> bool:

        index = bisect_left(self.arr, val)
        if index == len(self.arr) or self.arr[index] != val:
            return False

        del self.arr[index]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


def test(
    testObj: unittest.TestCase, actions: List, params: List, expected: List
) -> None:
    n = len(actions)
    obj = RandomizedCollection(*params[0])
    print("------------test case-----------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print("-------done-------------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "insert":
                actual_bool = obj.insert(*params[i])
                testObj.assertEqual(actual_bool, expected[i])

            case "remove":
                actual_bool = obj.remove(*params[i])
                testObj.assertEqual(actual_bool, expected[i])

            case "getRandom":
                actual_get_random = obj.getRandom(*params[i])
                testObj.assertEqual(actual_get_random, expected[i])


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            [
                "RandomizedCollection",
                "insert",
                "insert",
                "insert",
                "getRandom",
                "remove",
                "getRandom",
            ],
            [[], [1], [1], [2], [], [1], []],
            [None, True, False, True, 2, True, 1],
        )

    def test_2(self):
        test(
            self,
            [
                "RandomizedCollection",
                "insert",
                "remove",
                "insert",
                "getRandom",
                "remove",
                "insert",
                "getRandom",
            ],
            [[], [1], [2], [2], [], [1], [2], []],
            [None, True, False, True, 2, True, False, 2],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 457 ms, faster than 94.39%
Memory Usage: 64.6 MB, less than 95.77%
"""

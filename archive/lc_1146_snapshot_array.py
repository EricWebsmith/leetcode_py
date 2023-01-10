
import unittest
from collections import defaultdict
from typing import List


class SnapshotArray:

    def __init__(self, length: int) -> None:
        self.cur_snap_id = 0
        self.snaps: dict = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        if index in self.snaps[index] and self.snaps[index][-1][0] == self.cur_snap_id:
            self.snaps[index][-1] = (self.cur_snap_id, val)
            return
        self.snaps[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > self.cur_snap_id:
            return 0

        arr = self.snaps[index]
        if len(arr) == 0:
            return 0

        if arr[0][0] > snap_id:
            return 0
        left = 0
        right = len(arr) - 1
        while left < right:
            m = (left + right + 1) >> 1
            if arr[m][0] <= snap_id:
                left = m
            else:
                right = m - 1

        return self.snaps[index][left][1]


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = SnapshotArray(params[0][0])
    for i in range(1, n):
        match actions[i]:
            case "set":
                obj.set(*params[i])

            case "snap":
                actual_int = obj.snap(*params[i])
                testObj.assertEqual(actual_int, expected[i])

            case "get":
                actual_int = obj.get(*params[i])
                testObj.assertEqual(actual_int, expected[i])


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self, ["SnapshotArray", "set", "snap", "set", "get"], [
             [3], [0, 5], [], [0, 6], [0, 0]], [None, None, 0, None, 5])

    def test_2(self):
        test(self, ["SnapshotArray", "set", "snap", "snap", "snap", "get", "snap", "snap", "get"],
             [[1], [0, 15], [], [], [], [0, 2], [], [], [0, 0]],
             [None, None, 0, 1, 2, 15, 3, 4, 15]
             )


if __name__ == '__main__':
    unittest.main()

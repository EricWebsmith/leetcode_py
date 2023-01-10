import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms: list[int] = []
        intervals.sort(key=lambda x: x[0])
        heappush(rooms, intervals[0][1])  # type: ignore
        max_rooms = 1
        for start, end in intervals[1:]:
            while rooms and rooms[0] <= start:
                heappop(rooms)  # type: ignore

            heappush(rooms, end)  # type: ignore
            max_rooms = max(max_rooms, len(rooms))
        return max_rooms


def test(testObj: unittest.TestCase, intervals: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.minMeetingRooms(intervals)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[0, 30], [5, 10], [15, 20]], 2)

    def test_2(self):
        test(self,   [[7, 10], [2, 4]], 1)

    def test_3(self):
        test(self,   [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 86 ms, faster than 89.95%
Memory Usage: 17.5 MB, less than 83.51%
'''

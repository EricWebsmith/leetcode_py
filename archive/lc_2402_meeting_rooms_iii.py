import unittest
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms = [room_id for room_id in range(n)]
        heapify(unused_rooms)
        room_counts = [0] * n
        meetings.sort()
        h = []
        for start, end in meetings:
            # firstly, pop finished meetings.
            while h and h[0][0] <= start:
                _, room_id = heappop(h)
                heappush(unused_rooms, room_id)
            wait = 0

            # if no available room, pop meetings finish first.
            # if there are more than two, pop all.
            if not unused_rooms:
                prev_end, room_id = heappop(h)
                heappush(unused_rooms, room_id)
                wait = prev_end - start

            # now, we can have the meeting in the smallest meeting room.
            end += wait
            room_id = heappop(unused_rooms)
            heappush(h, (end, room_id))
            room_counts[room_id] += 1

        return room_counts.index(max(room_counts))


def test(testObj: unittest.TestCase, n: int, meetings: List[List[int]], expected: int) -> None:
    so = Solution()
    actual = so.mostBooked(n, meetings)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   2,  [[0, 10], [1, 5], [2, 7], [3, 4]], 0)

    def test_2(self):
        test(self,   3,  [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 1)

    # test case 75
    def test_3(self):
        test(self,   4,  [[10, 11], [13, 15], [9, 19], [0, 12], [12, 20]], 0)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
2139 ms
Beats
82.17%
'''

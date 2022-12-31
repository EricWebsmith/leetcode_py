import unittest
from bisect import bisect_right, insort_left
from typing import List


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        k = len(queries)
        rooms.sort(key=lambda x: x[1])
        queries = [(room_size, room_id, i)
                   for i, (room_id, room_size) in enumerate(queries)]
        queries.sort()
        ans = [-1] * k

        valid_room_ids = []
        while queries:
            min_size, pre_id, i = queries.pop()
            while rooms and rooms[-1][1] >= min_size:
                insort_left(valid_room_ids, rooms.pop()[0])

            if len(valid_room_ids) == 0:
                continue

            index = bisect_right(valid_room_ids, pre_id)
            if (index == len(valid_room_ids)) or index > 0 and \
                    pre_id - valid_room_ids[index-1] <= valid_room_ids[index] - pre_id:
                ans[i] = valid_room_ids[index-1]
            else:
                ans[i] = valid_room_ids[index]

        return ans


def test(testObj: unittest.TestCase, rooms: List[List[int]], queries: List[List[int]], expected: List[int]) -> None:

    so = Solution()

    actual = so.closestRoom(rooms, queries)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[2, 2], [1, 2], [3, 2]],  [
             [3, 1], [3, 3], [5, 2]], [3, -1, 3])

    def test_2(self):
        test(self,   [[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]],
             [[2, 3], [2, 4], [2, 5]], [2, 1, 3])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 2056 ms, faster than 100.00%
Memory Usage: 66 MB, less than 47.62%
'''

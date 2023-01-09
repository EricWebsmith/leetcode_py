import unittest

import sortedcontainers  # type: ignore

EVENT_START = 0
EVENT_END = 1


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for b in buildings:
            events.append((b[0], EVENT_START, b[2]))
            events.append((b[1], EVENT_END, b[2]))

        events = sorted(events, key=lambda x: (
            x[0], x[1], -x[2] if x[1] == EVENT_START else x[2]))

        print(events)

        result = []

        current_heights = sortedcontainers.SortedList([0])

        for x, event_type, height in events:
            if event_type == EVENT_START:
                if height > current_heights[-1]:
                    result.append([x, height])
                current_heights.add(height)
            else:
                current_heights.remove(height)
                if height > current_heights[-1]:
                    result.append([x, current_heights[-1]])

        return result


def test(testObj: unittest.TestCase, buildings: list[list[int]], expected: list[list[int]]) -> None:
    so = Solution()
    actual = so.getSkyline(buildings)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]], [
             [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])

    def test_2(self):
        test(self,   [[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]])

    def test_3(self):
        test(self,   [[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]])


if __name__ == '__main__':
    unittest.main()

'''
https://leetcode.com/problems/the-skyline-problem/solutions/955087/short-and-sweeet-sweep-line/
162ms, 80.59%
'''

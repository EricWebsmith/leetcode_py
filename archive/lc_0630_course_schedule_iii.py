import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        max_time = 0
        for time, end_time in courses:
            heappush(heap, -time)
            max_time += time
            if max_time > end_time:
                big_time = heappop(heap)
                max_time += big_time
        return len(heap)


def test(testObj: unittest.TestCase, courses: List[List[int]], expected: int) -> None:
    s = Solution()
    actual = s.scheduleCourse(courses)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self, [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3)

    def test_2(self):
        test(self, [[1, 2]], 1)

    def test_3(self):
        test(self, [[3, 2], [4, 3]], 0)


if __name__ == '__main__':
    unittest.main()

# Runtime: 741 ms, faster than 91.08%
# Memory Usage: 20.2 MB, less than 29.29%

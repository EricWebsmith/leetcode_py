from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
import itertools
null = None


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        g = [0] * n
        for pre, post in relations:
            g[post-1] ^= 1 << (pre-1)

        course_bitmasks = [1 << i for i in range(n)]

        # bitmask for all courses
        all_courses_bitmask = (1 << n) - 1

        # first is courses taken
        # if course 0 and 4 are taken, it will be 0b10001
        # second is semasters so for
        q = deque([(0, 0)])
        seen = [False] * (1 << n)

        while q:
            taken, semester = q.popleft()
            available = [course_bitmasks[i] for i in range(n) if (
                taken & g[i] == g[i]) and (taken & course_bitmasks[i] == 0)]
            if len(available) <= k:
                taken += sum(available)
                if taken == all_courses_bitmask:
                    return semester + 1
                if not seen[taken]:
                    q.append((taken, semester+1))
                    seen[taken] == True
            else:
                for batch in itertools.combinations(available, k):
                    t = taken ^ sum(batch)
                    if t == all_courses_bitmask:
                        return semester + 1
                    if not seen[t]:
                        q.append((t, semester+1))
                        seen[t] = 1


def test(testObj: unittest.TestCase, n: int, relations: List[List[int]], k: int, expected: int) -> None:
    so = Solution()
    actual = so.minNumberOfSemesters(n, relations, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   4,  [[2, 1], [3, 1], [1, 4]],  2, 3)

    def test_2(self):
        test(self,   5,  [[2, 1], [3, 1], [4, 1], [1, 5]],  2, 4)

    def test_3(self):
        test(self,   13,
             [[12, 8], [2, 4], [3, 7], [6, 8], [11, 8], [9, 4], [9, 7], [12, 4], [11, 4], [6, 4], [1, 4], [10, 7], [10, 4], [
                 1, 7], [1, 8], [2, 7], [8, 4], [10, 8], [12, 7], [5, 4], [3, 4], [11, 7], [7, 4], [13, 4], [9, 8], [13, 8]],
             9, 3)

    def test_4(self):
        test(self,   9,  [[2, 1], [3, 1], [4, 1], [
             1, 5], [5, 6], [6, 7], [1, 8], [1, 9]],  2, 6)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 827 ms, faster than 87.94% of Python3 online submissions for Parallel Courses II.
Memory Usage: 14.9 MB, less than 84.40% of Python3 online submissions for Parallel Courses II.
'''

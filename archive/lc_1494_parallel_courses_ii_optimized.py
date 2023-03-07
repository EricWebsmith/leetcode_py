import itertools
import unittest
from collections import deque


def bit_or(arr: list[int]):
    """
    not sure if this will make it faster.
    """
    ans = 0
    for num in arr:
        ans |= num
    return ans


class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        g = [0] * n
        prerequisites_bitmask = 0
        for pre, post in relations:
            g[post - 1] |= 1 << (pre - 1)
            prerequisites_bitmask |= 1 << (pre - 1)

        # course 1 is 1,
        # course 2 is 2,
        # course 3 is 4,
        # course 4 is 8,
        # and so on
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
            available = [
                course_bitmasks[i] for i in range(n) if (taken & g[i] == g[i]) and (taken & course_bitmasks[i] == 0)
            ]
            available_pres = [a for a in available if (a & prerequisites_bitmask) > 0]
            available_not_pres = [a for a in available if (a & prerequisites_bitmask) == 0]
            if len(available_pres) <= k:
                # it is not correct to use sum here.
                # if you take course 2 two times,
                # taken is still 2, not 4
                # we can use sum only because we rule out taken courses previously
                taken |= bit_or(available_pres) | bit_or(available_not_pres[: k - len(available_pres)])
                if taken == all_courses_bitmask:
                    return semester + 1
                if not seen[taken]:
                    q.append((taken, semester + 1))
                    seen[taken] = True
            else:
                for batch in itertools.combinations(available, k):
                    t = taken | bit_or(batch)  # type: ignore
                    if t == all_courses_bitmask:
                        return semester + 1
                    if not seen[t]:
                        q.append((t, semester + 1))
                        seen[t] = True

        return -1


def test(
    testObj: unittest.TestCase,
    n: int,
    relations: list[list[int]],
    k: int,
    expected: int,
) -> None:
    so = Solution()
    actual = so.minNumberOfSemesters(n, relations, k)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 4, [[2, 1], [3, 1], [1, 4]], 2, 3)

    def test_2(self):
        test(self, 5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2, 4)

    def test_3(self):
        test(
            self,
            13,
            [
                [12, 8],
                [2, 4],
                [3, 7],
                [6, 8],
                [11, 8],
                [9, 4],
                [9, 7],
                [12, 4],
                [11, 4],
                [6, 4],
                [1, 4],
                [10, 7],
                [10, 4],
                [1, 7],
                [1, 8],
                [2, 7],
                [8, 4],
                [10, 8],
                [12, 7],
                [5, 4],
                [3, 4],
                [11, 7],
                [7, 4],
                [13, 4],
                [9, 8],
                [13, 8],
            ],
            9,
            3,
        )

    def test_4(self):
        test(
            self,
            9,
            [[2, 1], [3, 1], [4, 1], [1, 5], [5, 6], [6, 7], [1, 8], [1, 9]],
            2,
            6,
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 75 ms, faster than 93.62%
Memory Usage: 14.1 MB, less than 95.74%
"""

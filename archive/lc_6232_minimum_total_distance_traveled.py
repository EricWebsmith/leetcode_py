import unittest
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        h: list = []
        factory.sort()
        robot.sort()
        for r in robot:
            for f, c in factory:
                d = abs(r - f)
                heappush(h, (d, r, f))  # type: ignore

        f_dict = dict()
        for f, c in factory:
            f_dict[f] = c

        ans = 0
        fixed_robots = set()
        while h:
            dis, r, f = heappop(h)
            if r in fixed_robots:
                continue
            if f_dict[f] > 0:
                f_dict[f] -= 1
                ans += dis
                fixed_robots.add(r)

        return ans


def test(testObj: unittest.TestCase, robot: List[int], factory: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.minimumTotalDistance(robot, factory)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [0, 4, 6],  [[2, 2], [6, 2]], 4)

    def test_2(self):
        test(self,   [1, -1],  [[-2, 1], [2, 1]], 2)

    def test_3(self):
        test(self,   [9, 11, 99, 101],
             [[10, 1], [7, 1], [14, 1], [100, 1], [96, 1], [103, 1]], 6)


if __name__ == '__main__':
    unittest.main()

'''

'''

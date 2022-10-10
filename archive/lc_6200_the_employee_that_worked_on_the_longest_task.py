import unittest
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        previous_time = 0
        time = 0
        ans = 0
        for employee, current_time in logs:
            new_time = current_time - previous_time
            if new_time > time:
                ans = employee
                time = new_time
            if new_time == time and employee < ans:
                ans = employee
            previous_time = current_time

        return ans


def test(testObj: unittest.TestCase, n: int, logs: List[List[int]], expected: int) -> None:

    so = Solution()

    actual = so.hardestWorker(n, logs)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   10,  [[0, 3], [2, 5], [0, 9], [1, 15]], 1)

    def test_2(self):
        test(self,   26,  [[1, 1], [3, 7], [2, 12], [7, 17]], 3)

    def test_3(self):
        test(self,   2,  [[0, 10], [1, 20]], 0)

    def test_4(self):
        test(self,   70,
             [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]], 12)


if __name__ == '__main__':
    unittest.main()

'''

'''

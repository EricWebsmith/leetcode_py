import unittest
from typing import Counter, List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        c = Counter(students)
        for i, s in enumerate(sandwiches):
            if c[s] == 0:
                return n - i

            c[s] -= 1

        return 0


def test(testObj: unittest.TestCase, students: List[int], sandwiches: List[int], expected: int) -> None:
    so = Solution()
    actual = so.countStudents(students, sandwiches)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 1, 0, 0],  [0, 1, 0, 1], 0)

    def test_2(self):
        test(self,   [1, 1, 1, 0, 0, 1],  [1, 0, 0, 0, 1, 1], 3)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
36 ms
Beats
96.94%
'''

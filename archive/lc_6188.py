import unittest
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        name_heights: list = []
        for i in range(n):
            name_heights.append((heights[i], names[i]))

        name_heights.sort()

        return [name for _, name in name_heights]


def test(testObj: unittest.TestCase, courses: List[List[int]], expected: int) -> None:
    s = Solution()
    actual = s.scheduleCourse(courses)  # type: ignore
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3)

    def test_2(self):
        test(self, [[1, 2]], 1)

    def test_3(self):
        test(self, [[3, 2], [4, 3]], 0)


if __name__ == "__main__":
    unittest.main()

# Runtime: 741 ms, faster than 91.08%
# Memory Usage: 20.2 MB, less than 29.29%

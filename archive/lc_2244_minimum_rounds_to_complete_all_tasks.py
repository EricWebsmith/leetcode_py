import unittest
from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)

        ans = 0
        for k, v in d.items():
            if v < 2:
                return -1
            ans += v // 3
            if v % 3 > 0:
                ans += 1
        return ans


def test(testObj: unittest.TestCase, tasks: List[int], expected: int) -> None:

    so = Solution()
    actual = so.minimumRounds(tasks)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, [2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4)

    def test_2(self):
        test(self, [2, 3, 3], -1)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 932 ms, faster than 99.47%
Memory Usage: 28.5 MB, less than 38.92%
"""

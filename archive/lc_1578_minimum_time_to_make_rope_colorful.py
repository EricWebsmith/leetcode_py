import unittest
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        previous_color = colors[0]
        max_time = neededTime[0]

        ans = 0
        for i in range(1, len(colors)):
            if colors[i] == previous_color:
                ans += min(neededTime[i], max_time)
                max_time = max(neededTime[i], max_time)
            else:
                max_time = neededTime[i]

            previous_color = colors[i]

        return ans


def test(testObj: unittest.TestCase, colors: str, neededTime: List[int], expected: int) -> None:

    so = Solution()
    actual = so.minCost(colors, neededTime)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "abaac", [1, 2, 3, 4, 5], 3)

    def test_2(self):
        test(self, "abc", [1, 2, 3], 0)

    def test_3(self):
        test(self, "aabaa", [1, 2, 3, 4, 1], 2)

    def test_4(self):
        test(self, "bbbaaa", [4, 9, 3, 8, 8, 9], 23)


if __name__ == "__main__":
    unittest.main()

"""
1246ms, 88.18%
"""

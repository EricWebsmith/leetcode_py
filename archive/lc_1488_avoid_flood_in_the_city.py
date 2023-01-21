import unittest
from bisect import bisect_right


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        clean_days: list = []
        d: dict = dict()
        ans = [-1] * n
        for i in range(n):
            if rains[i] == 0:
                clean_days.append(i)
                ans[i] = 1
            else:
                if rains[i] in d:
                    last_rain = d[rains[i]]
                    clean_day_index = bisect_right(clean_days, last_rain)
                    if clean_day_index == len(clean_days):
                        return []

                    ans[clean_days[clean_day_index]] = rains[i]
                    del clean_days[clean_day_index]
                d[rains[i]] = i

        return ans


def test(testObj: unittest.TestCase, rains: list[int], expected: int) -> None:

    so = Solution()
    actual = so.avoidFlood(rains)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, [1, 2, 3, 4], [-1, -1, -1, -1])

    def test_2(self):
        test(self, [1, 2, 0, 0, 2, 1], [-1, -1, 2, 1, -1, -1])

    def test_3(self):
        test(self, [1, 2, 0, 1, 2], [])

    def test_4(self):
        test(self, [69, 0, 0, 0, 69], [-1, 69, 1, 1, -1])

    def test_5(self):
        test(self, [0, 1, 1], [])

    def test_6(self):
        test(self, [1, 0, 2, 0, 2, 1], [-1, 1, -1, 2, -1, -1])


if __name__ == "__main__":
    unittest.main()

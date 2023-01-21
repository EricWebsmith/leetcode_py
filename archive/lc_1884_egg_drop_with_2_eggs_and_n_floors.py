import unittest


class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp_first_drop = [0, 1, 1, 2, 2]
        dp = [0, 1, 2, 2, 3]
        for i in range(5, n + 1):
            # drop 1
            first_drop_1 = dp_first_drop[i - 1]
            # first drop breaks
            break_drops_1 = first_drop_1 + 1
            # first drop does not break
            not_break_drops_1 = dp[i - first_drop_1 - 1] + 1
            drops_1 = max(break_drops_1, not_break_drops_1)

            # drop 2
            first_drop_2 = dp_first_drop[i - 1] + 1
            # first drop breaks
            break_drops_2 = first_drop_2 + 1
            # first drop does not break
            not_break_drops_2 = dp[i - first_drop_2 - 1] + 1
            drops_2 = max(break_drops_2, not_break_drops_2)

            if drops_2 <= drops_1:
                dp_first_drop.append(first_drop_2)
                dp.append(drops_2)
            else:
                dp_first_drop.append(first_drop_1)
                dp.append(drops_1)

        return dp[n]


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()
    actual = so.twoEggDrop(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 1, 1)

    def test_2(self):
        test(self, 2, 2)

    def test_3(self):
        test(self, 3, 2)

    def test_4(self):
        test(self, 4, 3)

    def test_5(self):
        test(self, 5, 3)

    def test_10(self):
        test(self, 10, 4)

    def test_99(self):
        test(self, 100, 14)

    def test_100(self):
        test(self, 100, 14)

    def test_101(self):
        test(self, 101, 14)

    def test_345(self):
        test(self, 345, 26)

    def test_999(self):
        test(self, 999, 45)

    def test_1000(self):
        test(self, 1000, 45)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 46 ms, faster than 77.25%
Memory Usage: 13.9 MB, less than 70.75%
"""

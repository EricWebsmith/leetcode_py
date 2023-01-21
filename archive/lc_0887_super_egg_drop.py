import unittest


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        dp(i,j) with i eggs and j allowed steps, the max floor one can test to certain f
        dp(i, j) = dp(i - 1, j - 1) + 1 + dp(i, j - 1)
        dp(0, j) = 0
        dp(i, 0) = 0
        min j that makes dp(k, j) >= n
        """
        memo = [[0] * (n + 1) for _ in range(k + 1)]

        for j in range(1, n + 1):
            for i in range(1, k + 1):
                memo[i][j] = memo[i - 1][j - 1] + 1 + memo[i][j - 1]
                if i == k and memo[i][j] >= n:
                    return j
        return -1


def test(testObj: unittest.TestCase, k: int, n: int, expected: int) -> None:

    so = Solution()
    actual = so.superEggDrop(k, n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1_2(self):
        test(self, 1, 2, 2)

    def test_2_1(self):
        test(self, 2, 1, 1)

    def test_2_2(self):
        test(self, 2, 2, 2)

    def test_2_3(self):
        test(self, 2, 3, 2)

    def test_2_4(self):
        test(self, 2, 4, 3)

    def test_2_5(self):
        test(self, 2, 5, 3)

    def test_2_10(self):
        test(self, 2, 10, 4)

    def test_2_99(self):
        test(self, 2, 100, 14)

    def test_2_100(self):
        test(self, 2, 100, 14)

    def test_2_101(self):
        test(self, 2, 101, 14)

    def test_2_345(self):
        test(self, 2, 345, 26)

    def test_2_999(self):
        test(self, 2, 999, 45)

    def test_2_1000(self):
        test(self, 2, 1000, 45)

    def test_3_1(self):
        test(self, 3, 1, 1)

    def test_3_2(self):
        test(self, 3, 2, 2)

    def test_3_3(self):
        test(self, 3, 3, 2)

    def test_3_4(self):
        test(self, 3, 4, 3)

    def test_3_5(self):
        test(self, 3, 5, 3)

    def test_3_6(self):
        test(self, 3, 6, 3)

    def test_3_7(self):
        test(self, 3, 7, 3)

    def test_3_14(self):
        test(self, 3, 14, 4)

    def test_3_100(self):
        test(self, 3, 100, 9)

    def test_3_200(self):
        test(self, 3, 200, 11)

    def test_3_1000(self):
        test(self, 3, 1000, 19)


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 65 ms, faster than 80.11%
Memory Usage: 20.4 MB, less than 68.11%
"""

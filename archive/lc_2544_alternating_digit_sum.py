import unittest


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        s = 0
        while n > 0:
            s += sign * (n % 10)
            n = n // 10
            sign *= -1

        return -sign * s


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:
    so = Solution()
    actual = so.alternateDigitSum(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 521, 4)

    def test_2(self):
        test(self, 111, 1)

    def test_3(self):
        test(self, 886996, 0)


if __name__ == "__main__":
    unittest.main()


"""
Runtime
55 ms
Beats
87.50%
"""

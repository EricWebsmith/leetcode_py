import unittest


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        if n == 1:
            return True

        return (n + 3) == (n | 3)


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()
    actual = so.isPowerOfFour(n)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        test(self, 16, True)

    def test_2(self):
        test(self, 5, False)

    def test_3(self):
        test(self, 1, True)

    def test_4(self):
        test(self, 32, True)


if __name__ == "__main__":
    unittest.main()

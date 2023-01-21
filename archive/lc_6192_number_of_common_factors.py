import unittest


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for c in range(1, min(a, b) + 1):
            if a % c == 0 and b % c == 0:
                ans += 1

        return ans


def test(testObj: unittest.TestCase, a: int, b: int, expected: int) -> None:
    so = Solution()
    actual = so.commonFactors(a, b)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 12, 6, 4)

    def test_2(self):
        test(self, 25, 30, 2)


if __name__ == "__main__":
    unittest.main()

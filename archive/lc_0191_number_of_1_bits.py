import unittest

null = None


class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        ans = 0
        while n > 0:
            n = n & (n - 1)
            ans += 1

        return ans


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:
    so = Solution()
    actual = so.hammingWeight(n)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 11, 3)

    def test_2(self):
        test(self, 128, 1)

    def test_3(self):
        test(self, 2**32 - 1 - 2, 31)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
40 ms
Beats
81.51%
"""

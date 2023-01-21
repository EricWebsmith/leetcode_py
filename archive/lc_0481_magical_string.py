import unittest


class Solution:
    def magicalString(self, n: int) -> int:
        s = "12211"
        p = 3
        while len(s) < n:
            new_char = "1" if s[-1] == "2" else "2"
            if s[p] == "1":
                s = s + new_char
            else:
                s = s + new_char + new_char
            p += 1

        s = s[:n]
        ans = 0
        for c in s:
            if c == "1":
                ans += 1

        return ans


def test(testObj: unittest.TestCase, n: int, expected: int) -> None:

    so = Solution()

    actual = so.magicalString(n)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, 6, 3)

    def test_2(self):
        test(self, 1, 1)

    def test_3(self):
        test(self, 200, 100)

    def test_4(self):
        test(self, 300, 150)

    def test_5(self):
        test(self, 301, 151)

    def test_6(self):
        test(self, 302, 151)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
272 ms
Beats
61.85%
"""

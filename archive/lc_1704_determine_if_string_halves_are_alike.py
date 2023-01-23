import unittest


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        n = len(s)
        return sum([c in vowels for c in s[: n // 2]]) == sum([c in vowels for c in s[n // 2 :]])


def test(testObj: unittest.TestCase, s: str, expected: bool) -> None:
    so = Solution()
    actual = so.halvesAreAlike(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "book", True)

    def test_2(self):
        test(self, "textbook", False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
53 ms
Beats
75.49%
"""

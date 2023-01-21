import unittest


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        initial_capital = word[0].isupper()
        is_capital = word[1].isupper()
        for c in word[2:]:
            if c.isupper() != is_capital:
                return False

        if not initial_capital and is_capital:
            return False

        return True


def test(testObj: unittest.TestCase, word: str, expected: bool) -> None:
    so = Solution()
    actual = so.detectCapitalUse(word)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, "USA", True)

    def test_2(self):
        test(self, "FlaG", False)

    def test_3(self):
        test(self, "leetcode", True)

    def test_4(self):
        test(self, "Google", True)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
34 ms
Beats
84.76%
"""

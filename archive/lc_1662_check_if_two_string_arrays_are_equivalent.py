import unittest
from typing import Generator, List


def generate_chars(word_arr: List[str]) -> Generator[str, None, None]:
    for word in word_arr:
        for c in word:
            yield c
    yield " "


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        g1 = generate_chars(word1)
        g2 = generate_chars(word2)
        for c1, c2 in zip(g1, g2):
            if c1 != c2:
                return False

        return True


def test(testObj: unittest.TestCase, word1: List[str], word2: List[str], expected: bool) -> None:
    so = Solution()
    actual = so.arrayStringsAreEqual(word1, word2)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, ["ab", "c"], ["a", "bc"], True)

    def test_2(self):
        test(self, ["a", "cb"], ["ab", "c"], False)

    def test_3(self):
        test(self, ["abc", "d", "defg"], ["abcddefg"], True)

    def test_4(self):
        test(self, ["a", "bc"], ["ab", "cc"], False)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
23 ms
Beats
99.86%
"""

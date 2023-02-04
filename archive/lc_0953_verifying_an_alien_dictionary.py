import unittest


def compare(s1: str, s2: str, d: dict[str, int]) -> int:
    for c1, c2 in zip(s1, s2):
        if d[c1] > d[c2]:
            return 1
        elif d[c1] < d[c2]:
            return -1

    return len(s1) - len(s2)


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            if compare(words[i], words[i + 1], d) >= 1:
                return False

        return True


def test(testObj: unittest.TestCase, words: list[str], order: str, expected: bool) -> None:
    so = Solution()
    actual = so.isAlienSorted(words, order)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True)

    def test_2(self):
        test(self, ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False)

    def test_3(self):
        test(self, ["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False)


if __name__ == "__main__":
    unittest.main()


"""

"""

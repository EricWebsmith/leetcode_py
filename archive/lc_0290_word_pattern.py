import unittest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        seen_pattern = set()
        word_to_pattern = {}

        for word, p in zip(words, pattern):
            if word in word_to_pattern:
                if word_to_pattern[word] != p:
                    return False
            else:
                if p in seen_pattern:
                    return False
                word_to_pattern[word] = p
                seen_pattern.add(p)

        return True


def test(testObj: unittest.TestCase, pattern: str, s: str, expected: bool) -> None:
    so = Solution()
    actual = so.wordPattern(pattern, s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "abba",  "dog cat cat dog", True)

    def test_2(self):
        test(self,   "abba",  "dog cat cat fish", False)

    def test_3(self):
        test(self,   "aaaa",  "dog cat cat dog", False)

    def test_4(self):
        test(self,   "e",  "eukera", True)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
27 ms
Beats
95.33%
'''

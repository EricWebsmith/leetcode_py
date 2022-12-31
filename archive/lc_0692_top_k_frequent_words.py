import unittest
from typing import Counter, List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        keys = list(c.keys())
        keys.sort(key=lambda w: (-c[w], w))
        return keys[:k]


def test(testObj: unittest.TestCase, words: List[str], k: int, expected: List[str]) -> None:

    so = Solution()

    actual = so.topKFrequent(words, k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["i", "love", "leetcode", "i",
             "love", "coding"],  2, ["i", "love"])

    def test_2(self):
        test(self,   ["the", "day", "is", "sunny", "the", "the", "the",
             "sunny", "is", "is"],  4, ["the", "is", "sunny", "day"])


if __name__ == '__main__':
    unittest.main()

'''

'''

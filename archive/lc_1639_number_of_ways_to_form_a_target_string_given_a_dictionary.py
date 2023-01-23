import unittest
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(words[0])
        word_counters: list = []
        for j in range(m):
            counter = defaultdict(int)
            for word in words:
                counter[word[j]] += 1
            word_counters.append(counter)

        n = len(target)

        @cache
        def dfs(i: int, j: int):
            left = n - i
            if left == 0:
                return 1
            if n - i > m - j:
                return 0
            return word_counters[j][target[i]] * dfs(i + 1, j + 1) + dfs(i, j + 1)

        return dfs(0, 0) % 1_000_000_007


def test(testObj: unittest.TestCase, words: List[str], target: str, expected: int) -> None:

    so = Solution()
    actual = so.numWays(words, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, ["acca", "bbbb", "caca"], "aba", 6)

    def test_2(self):
        test(self, ["abba", "baab"], "bab", 4)


if __name__ == "__main__":
    unittest.main()

"""
Runtime
1338 ms
Beats
91.44%
"""

import unittest
from typing import List

ascii_a = 97


class TrieNode:
    """
    lowercase letters only
    """

    def __init__(self) -> None:
        self.children: List[TrieNode] = [None] * 26  # type: ignore
        self.is_word = False

    @classmethod
    def add_word(cls, root: "TrieNode", word: str):
        current = root
        for c in word:
            index = ord(c) - ascii_a
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_word = True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        words.sort(key=lambda x: len(x))

        for word in words:
            TrieNode.add_word(root, word)

        q = [(root, "")]
        ans = ""
        while q:
            ans = q[0][1]
            new_q: list = []
            for parent, prefix in q:
                for index, child in enumerate(parent.children):
                    if child and child.is_word:
                        new_q.append((child, prefix + chr(ascii_a + index)))
            q = new_q

        return ans


def test(testObj: unittest.TestCase, words: List[str], expected: str) -> None:

    so = Solution()

    actual = so.longestWord(words)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    def test_1(self):
        test(self, ["k", "ki", "kir", "kira", "kiran"], "kiran")

    def test_2(self):
        test(self, ["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple")

    def test_3(self):
        test(self, ["abc", "bc", "ab", "qwe"], "")


if __name__ == "__main__":
    unittest.main()

"""
Runtime: 1171 ms, faster than 25.89%
Memory Usage: 57.3 MB, less than 5.58%
"""

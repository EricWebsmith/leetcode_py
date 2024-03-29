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
        for i, c in enumerate(word):
            index = ord(c) - ascii_a
            # here is the optimization
            # we only add a word when the prefixes exist.
            if i < len(word) - 1 and current.children[index] is None:
                return
            if i == len(word) - 1 and current.children[index] is None:
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
            # for each bfs iteration,
            # we take the first as the answer
            # because Trie is lexicographically ordered.
            ans = q[0][1]
            new_q: list = []
            for parent, prefix in q:
                for index, child in enumerate(parent.children):
                    if child:
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
Runtime: 777 ms, faster than 42.13%
Memory Usage: 17.4 MB, less than 80.71%
"""

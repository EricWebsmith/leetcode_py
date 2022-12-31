import unittest
from typing import Dict, List


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.count = 0
        self.count_end = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current.children[c].count += 1
            current = current.children[c]
        current.count_end += 1

    def countWordsEqualTo(self, word: str) -> int:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        return current.count_end

    def countWordsStartingWith(self, prefix: str) -> int:
        current = self.root
        for c in prefix:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        return current.count

    def erase(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current.children[c].count -= 1
            current = current.children[c]
        current.count_end -= 1


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = Trie(*params[0])
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "insert":
                actual = obj.insert(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "countWordsEqualTo":
                actual = obj.countWordsEqualTo(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "countWordsStartingWith":
                actual = obj.countWordsStartingWith(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "erase":
                actual = obj.erase(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase",
                    "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"],
             [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]],
             [None, None, None, 2, 2, None, 1, 1, None, 0])


if __name__ == '__main__':
    unittest.main()

# non-existant word will not be removed
# leetcode will say : 'erase' arguments are invalid: expected 'erase existing word' to have value from 1 to 100000 only

'''
Runtime: 355 ms, faster than 91.22%
Memory Usage: 28.6 MB, less than 50.00%
'''

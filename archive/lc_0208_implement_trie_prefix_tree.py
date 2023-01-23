import unittest
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict = dict()
        self.endOfWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = Trie(*params[0])
    print("------------test case-----------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print("-------done-------------")
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "insert":
                obj.insert(*params[i])

            case "search":
                actual = obj.search(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "startsWith":
                actual = obj.startsWith(*params[i])
                testObj.assertEqual(actual, expected[i])


class TestClass(unittest.TestCase):
    def test_1(self):
        test(
            self,
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
        )


if __name__ == "__main__":
    unittest.main()

"""
Runtime
345 ms
Beats
61.8%
"""

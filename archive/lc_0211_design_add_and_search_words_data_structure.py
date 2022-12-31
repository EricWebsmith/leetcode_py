import unittest
from typing import Dict, List


class WordDictionary:
    """
    Sovle Leetcode 211 using prefix and postfix.
    """

    def __init__(self):
        self.prefix: Dict[str, Dict[str]] = {}
        self.postfix: Dict[str, Dict[str]] = {}

    def addWord(self, word: str) -> None:
        # prefix
        node = self.prefix
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True

        # postfix
        node = self.postfix
        for c in reversed(list(word)):
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True

    def search(self, word: str) -> bool:
        chars = list(word)

        def search_in_node(chars, node) -> bool:
            for i, ch in enumerate(chars):
                if ch not in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(chars[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        n = len(chars)
        i = 0
        use_prefix = True
        while i < n // 2:
            if chars[i] == '.' and chars[n-1-i] != '.':
                use_prefix = False
                break
            if chars[i] != '.' and chars[n-1-i] == '.':
                use_prefix = True
                break
            i += 1

        # return search_in_node(chars, self.prefix)

        if use_prefix:
            return search_in_node(chars, self.prefix)
        else:
            chars.reverse()
            return search_in_node(chars, self.postfix)


def test(testObj: unittest.TestCase, actions: List, params: List, expected: List) -> None:
    n = len(actions)
    obj = WordDictionary(*params[0])
    print('------------test case-----------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
    print('-------done-------------')
    for i in range(1, n):
        print(i, actions[i], params[i], expected[i])
        match actions[i]:

            case "addWord":
                actual = obj.addWord(*params[i])
                testObj.assertEqual(actual, expected[i])

            case "search":
                actual = obj.search(*params[i])
                testObj.assertEqual(actual, expected[i])


def test2(testObj: unittest.TestCase, actions: List, params: List) -> None:
    n = len(actions)
    obj = WordDictionary(*params[0])
    for i in range(1, n):
        match actions[i]:

            case "addWord":
                obj.addWord(*params[i])

            case "search":
                obj.search(*params[i])


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self, ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
             [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
             [None, None, None, None, False, True, True, True])

    def test_2(self):
        operations = ['WordDictionary']
        args = [[]]
        chars = 'abcdefghijklmnopqrstuvwxy'
        for a in chars:
            for b in chars:
                for c in chars:
                    word = a+b+c
                    operations.append('addWord')
                    args.append([word])

        for i in range(10000):
            operations.append('search')
            args.append(['..z'])
        test2(self, operations, args)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
1781 ms
Beats
99.32%
'''

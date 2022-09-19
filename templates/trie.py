from typing import List


class TrieNode:
    """
    lowercase letters only
    """

    def __init__(self) -> None:
        self.children: List[TrieNode] = [None] * 26
        self.is_word = False

    @classmethod
    def add_word(cls, root: 'TrieNode', word: str):
        current = root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] == None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_word = True

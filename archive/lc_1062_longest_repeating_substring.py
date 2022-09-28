import unittest
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:

    def __init__(self) -> None:
        self.n = 0
        self.s = ''

    def search(self, m: int):
        subs = set()
        for end in range(m, self.n+1):
            start = end - m
            t = self.s[start:end]
            if t in subs:
                return True
            subs.add(t)

        return False

    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        self.s = s
        self.n = n

        left = 0
        right = n
        while left < right:
            m = (left + right+1) >> 1
            if self.search(m):
                left = m
            else:
                right = m - 1

        return left


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()

    actual = so.longestRepeatingSubstring(s)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "abcd", 0)

    def test_2(self):
        test(self,   "abbaba", 2)

    def test_3(self):
        test(self,   "aabcaabdaab", 3)

    def test_4(self):
        test(self,   "ababdababd", 5)

    def test_5(self):
        test(self,   "aaaaa", 4)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 34 ms, faster than 99.07% of Python3 online submissions for Longest Repeating Substring.
Memory Usage: 14.4 MB, less than 63.55% of Python3 online submissions for Longest Repeating Substring.
'''

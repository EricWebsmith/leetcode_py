import unittest
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        new_s = s + '*' + rev_s

        dp = [0] * len(new_s)

        for i in range(1, len(new_s)):
            j = dp[i-1]
            while j > 0 and new_s[j] != new_s[i]:
                j = dp[j-1]
            if new_s[i] == new_s[j]:
                dp[i] = j+1

        return rev_s[:n-dp[-1]] + s


def test(testObj: unittest.TestCase, s: str, expected: int) -> None:

    so = Solution()
    actual = so.shortestPalindrome(s)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   "aacecaaa", "aaacecaaa")

    def test_2(self):
        test(self,   "abcd", "dcbabcd")


if __name__ == '__main__':
    unittest.main()

'''

'''

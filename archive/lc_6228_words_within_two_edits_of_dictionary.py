import unittest
from typing import List

from data_structure.binary_tree import (TreeNode, array_to_treenode,
                                        treenode_to_array)
from data_structure.link_list import (ListNode, array_to_listnode,
                                      listnode_to_array)
from data_structure.nary_tree import Node, array_to_node, node_to_array

null = None


def is_similar(s: str, t: str):
    ans = 0
    for a, b in zip(s, t):
        if a != b:
            ans += 1
        if ans == 3:
            return False

    return True


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for d in dictionary:
                if is_similar(q, d):
                    ans.append(q)
                    break

        return ans


def test(testObj: unittest.TestCase, queries: List[str], dictionary: List[str], expected: List[str]) -> None:

    so = Solution()

    actual = so.twoEditWords(queries, dictionary)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["word", "note", "ants", "wood"],  [
             "wood", "joke", "moat"], ["word", "note", "wood"])

    def test_2(self):
        test(self,   ["yes"],  ["not"], [])


if __name__ == '__main__':
    unittest.main()

'''

'''

from heapq import heappop, heappush
import unittest
from functools import cache
from typing import List, Optional, Dict, Set, Any
from math import sqrt
from collections import deque, defaultdict
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(set)
        for path in paths:
            folder, *file_contents = path.split(' ')
            for file_content in file_contents:
                file, content = file_content.split('(')
                dic[content].add(folder+"/"+file)

        ans = []
        for _, val in dic.items():
            if len(val) > 1:
                ans.append(list(val))

        return ans


def test(testObj: unittest.TestCase, paths: List[str], expected: List[List[str]]) -> None:

    so = Solution()

    actual = so.findDuplicate(paths)
    actual.sort()
    for a in actual:
        a.sort()
    expected.sort()
    for e in expected:
        e.sort()
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)",
             "root 4.txt(efgh)"], [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]])

    def test_2(self):
        test(self,   ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"],
             [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]])


if __name__ == '__main__':
    unittest.main()

'''

'''

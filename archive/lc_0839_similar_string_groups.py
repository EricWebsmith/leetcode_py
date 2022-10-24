import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def merge(self, x: int, y: int) -> int:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 1

        if py > px:
            self.p[py] = px
        else:
            self.p[px] = py
        self.e += 1
        return 0


class Solution:
    def simialr(self, a: str, b: str) -> bool:
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
                # this make it 10 times faster.
                if diff > 2:
                    return False
        return diff <= 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        dsu = DSU(n)
        for i in range(n):
            for j in range(i+1, n):
                if self.simialr(strs[i], strs[j]):
                    dsu.merge(i, j)

        pset = set()
        for i in range(n):
            p = dsu.find(i)
            pset.add(p)

        return len(pset)


def test(testObj: unittest.TestCase, strs: List[str], expected: int) -> None:

    so = Solution()
    actual = so.numSimilarGroups(strs)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   ["tars", "rats", "arts", "star"], 2)

    def test_2(self):
        test(self,   ["omv", "ovm"], 1)

    def test_3(self):
        test(self,   ["tars", "rats", "arts", "star", 'start'], 2)

    def test_4(self):
        test(self,   ["abc", "acb", "bca", "bac"], 1)

    def test_5(self):
        test(self,   ["ajdidocuyh", "djdyaohuic", "ddjyhuicoa", "djdhaoyuic", "ddjoiuycha",
             "ddhoiuycja", "ajdydocuih", "ddjiouycha", "ajdydohuic", "ddjyouicha"], 2)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 269 ms, faster than 95.82% of Python3 online submissions for Similar String Groups.
Memory Usage: 14.3 MB, less than 63.11% of Python3 online submissions for Similar String Groups.
'''

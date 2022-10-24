import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.n = len(v1) + len(v2)
        v1.reverse()
        v2.reverse()
        self.it = self.iter()

    def iter(self):
        lists = [self.v1, self.v2]
        v1_exausted = False
        v2_exausted = False
        while not v1_exausted or not v2_exausted:
            for v in lists:
                if len(v) == 0 and v == self.v1:
                    v1_exausted = True
                if len(v) == 0 and v == self.v2:
                    v2_exausted = True

                if v1_exausted and v2_exausted:
                    break

                if len(v) > 0:
                    yield v.pop()

    def next(self) -> int:
        self.n -= 1
        return next(self.it)

    def hasNext(self) -> bool:
        return self.n > 0


def test(testObj: unittest.TestCase, v1: List[int], v2: List[int], expected: List[int]) -> None:
    i = ZigzagIterator(v1, v2)
    actual = []
    while i.hasNext():
        actual.append(i.next())
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2],  [3, 4, 5, 6], [1, 3, 2, 4, 5, 6])

    def test_2(self):
        test(self,   [1],  [], [1])

    def test_3(self):
        test(self,   [],  [1], [1])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 54 ms, faster than 88.03% of Python3 online submissions for Zigzag Iterator.
Memory Usage: 14.5 MB, less than 7.28% of Python3 online submissions for Zigzag Iterator.
'''

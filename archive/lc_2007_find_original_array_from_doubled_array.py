import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []

        changed.sort()

        original = []
        original_index = 0
        double = []
        for v in changed:
            if original and original_index < len(original) and original[original_index] * 2 == v:
                double.append(v)
                original_index += 1
            else:
                original.append(v)

        if len(original) == len(double):
            return original
        else:
            return []


def test(testObj: unittest.TestCase, changed: List[int], expected: List[int]) -> None:

    so = Solution()

    actual = so.findOriginalArray(changed)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 3, 4, 2, 6, 8], [1, 3, 4])

    def test_2(self):
        test(self,   [6, 3, 0, 1], [])

    def test_3(self):
        test(self,   [1], [])

    def test_4(self):
        test(self,   [1, 2], [1])

    def test_5(self):
        test(self,   [1, 2, 2, 4], [1, 2])

    def test_6(self):
        test(self,   [1, 2, 3, 4], [])

    def test_7(self):
        test(self,   [1, 2, 3, 4, 2, 4, 6, 8], [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1500 ms, faster than 92.68% of Python3 online submissions for Find Original Array From Doubled Array.
Memory Usage: 28.7 MB, less than 98.54% of Python3 online submissions for Find Original Array From Doubled Array.
'''

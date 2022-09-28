import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        for i in range(m):
            p.append(i+1)

        ans = []
        for q in queries:
            i = p.index(q)
            ans.append(i)
            p = [p[i]]+p[:i]+p[i+1:]

        return ans


def test(testObj: unittest.TestCase, queries: List[int], m: int, expected: int) -> None:

    so = Solution()
    actual = so.processQueries(queries, m)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [3, 1, 2, 1],  5, [2, 1, 2, 1])

    def test_2(self):
        test(self,   [4, 1, 2, 2],  4, [3, 1, 2, 0])

    def test_3(self):
        test(self,   [7, 5, 5, 8, 3],  8, [6, 5, 0, 7, 5])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 93 ms, faster than 69.50% of Python3 online submissions for Queries on a Permutation With Key.
Memory Usage: 14.1 MB, less than 47.52% of Python3 online submissions for Queries on a Permutation With Key.
'''

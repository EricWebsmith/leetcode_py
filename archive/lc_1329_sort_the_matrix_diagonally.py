import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for c_start in range(n):
            r = 0
            c = c_start
            arr = []
            while c < n and r < m:
                arr.append(mat[r][c])
                c += 1
                r += 1

            arr.sort()
            r = 0
            c = c_start
            i = 0
            while c < n and r < m:
                mat[r][c] = arr[i]
                c += 1
                r += 1
                i += 1

        for r_start in range(m):
            r = r_start
            c = 0
            arr = []
            while c < n and r < m:
                arr.append(mat[r][c])
                c += 1
                r += 1

            arr.sort()
            r = r_start
            c = 0
            i = 0
            while c < n and r < m:
                mat[r][c] = arr[i]
                c += 1
                r += 1
                i += 1

        return mat


def test(testObj: unittest.TestCase, mat: List[List[int]], expected: int) -> None:

    so = Solution()
    actual = so.diagonalSort(mat)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]],
             [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]])

    def test_2(self):
        test(self,   [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]], [
             [5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69], [14, 23, 25, 44, 58, 15], [22, 27, 31, 36, 50, 66], [84, 28, 75, 33, 55, 68]])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 95 ms, faster than 85.06% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 14.2 MB, less than 95.10% of Python3 online submissions for Sort the Matrix Diagonally.
'''

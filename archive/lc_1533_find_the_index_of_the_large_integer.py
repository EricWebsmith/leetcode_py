import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


class ArrayReader(object):
    # Compares the sum of arr[l..r] with the sum of arr[x..y]
    # return 1 if sum(arr[l..r]) > sum(arr[x..y])
    # return 0 if sum(arr[l..r]) == sum(arr[x..y])
    # return -1 if sum(arr[l..r]) < sum(arr[x..y])

    def __init__(self, arr) -> None:
        self.arr = arr

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        left = sum(self.arr[l: r+1])
        right = sum(self.arr[x: y+1])
        if left>right:
            return 1
        if left == right:
            return 0
        
        return -1

        # Returns the length of the array
    def length(self) -> int:
        return len(self.arr)


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        left = 0
        right = n - 1

        while left < right:
            m1 = (left + right) >> 1
            m2 = left + right - m1
            c = reader.compareSub(left, m1, m2, right)
            if c == 0:
                return m1
            if c>0:
                right = m1
            else:
                left = m2

        return left


def test(testObj: unittest.TestCase, arr: List[int], expected: int) -> None:

    reader = ArrayReader(arr)
    so = Solution()
    actual = so.getIndex(reader)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [7, 7, 7, 7, 10, 7, 7, 7], 4)

    def test_2(self):
        test(self,   [6, 6, 12], 2)

    def test_3(self):
        test(self,   [1,1,1,1,1,1,2,1,1], 6)


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 300 ms, faster than 85.50% of Python3 online submissions for Find the Index of the Large Integer.
Memory Usage: 54 MB, less than 51.14% of Python3 online submissions for Find the Index of the Large Integer.
'''

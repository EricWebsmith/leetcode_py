import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        j = 0
        k = 0

        ans = []
        for i in range(len(arr1)):
            while j < len(arr2) and arr2[j] < arr1[i]:
                j += 1
            if j == len(arr2) or arr2[j] != arr1[i]:
                continue

            while k < len(arr3) and arr3[k] < arr1[i]:
                k += 1

            if k == len(arr3) or arr3[k] != arr1[i]:
                continue

            ans.append(arr1[i])

        return ans


def test(testObj: unittest.TestCase, arr1: List[int], arr2: List[int], arr3: List[int], expected: int) -> None:

    so = Solution()
    actual = so.arraysIntersection(arr1, arr2, arr3)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [1, 2, 3, 4, 5],  [
             1, 2, 5, 7, 9],  [1, 3, 4, 5, 8], [1, 5])

    def test_2(self):
        test(self,   [197, 418, 523, 876, 1356],  [
             501, 880, 1593, 1710, 1870],  [521, 682, 1337, 1395, 1764], [])


if __name__ == '__main__':
    unittest.main()

'''
Runtime: 111 ms, faster than 75.72% of Python3 online submissions for Intersection of Three Sorted Arrays.
Memory Usage: 14.2 MB, less than 84.10% of Python3 online submissions for Intersection of Three
'''

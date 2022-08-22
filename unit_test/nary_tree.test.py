
from heapq import heappop, heappush
import unittest
from typing import List
from data_structure.nary_tree import Node, array_to_node, node_to_array


def test(testObj: unittest.TestCase, nums: List[int]) -> None:
    root = array_to_node(nums)
    actual = node_to_array(root)

    testObj.assertEqual(actual, nums)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  [1, None, 3, 2, 4, None, 5, 6])

    def test_2(self):
        test(self,  [1, None, 2])

    def test_3(self):
        test(self,  [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None,
             9, 10, None, None, 11, None, 12, None, 13, None, None, 14])

    def test_4(self):
        test(self,  [1, None, 2, 2, None, 3, None, 3])


if __name__ == '__main__':
    unittest.main()

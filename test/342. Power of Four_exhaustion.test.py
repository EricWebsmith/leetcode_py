from heapq import heappop, heappush
import unittest
from typing import List, Optional
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def print4(self):
        l = []
        for i in range(0, 16):
            l.append(4**i)

        print(l)
        # [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]

    def isPowerOfFour(self, n: int) -> bool:
        return n in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]


def test(testObj: unittest.TestCase, n: int, expected:int) -> None:
    
    so = Solution()
    actual = so.isPowerOfFour(n)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  16, True)

    def test_2(self):
        test(self,  5, False)

    def test_3(self):
        test(self,  1, True)
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 25 ms, faster than 99.41% of Python3 online submissions for Power of Four.
Memory Usage: 14 MB, less than 10.18% of Python3 online submissions for Power of Four.
"""        
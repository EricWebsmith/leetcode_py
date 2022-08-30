from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1:
            return n
        
        dp = list(range(0, n+1))
        for kk in range(2, k+1):
            next_dp = [0]
            prev_first_drop = 1
            for i in range(1, n+1):
                if i == 1 or i == 2:
                    next_dp.append(i)
                else:
                    # first drop = previous first_drop
                    first_drop = prev_first_drop
                    first_break = 1 + dp[first_drop-1]
                    first_not_break = 1 + next_dp[i - first_drop]
                    plan_1 = max(first_break, first_not_break)

                    first_drop = prev_first_drop + 1
                    first_break = 1 + dp[first_drop-1]
                    first_not_break = 1 + next_dp[i - first_drop]
                    plan_2 = max(first_break, first_not_break)

                    if plan_2<=plan_1:
                        next_dp.append(plan_2)
                        prev_first_drop = prev_first_drop + 1
                    else:
                        next_dp.append(plan_1)

            dp = next_dp

        return dp[n]


def test(testObj: unittest.TestCase, k: int, n: int, expected:int) -> None:
    
    so = Solution()
    actual = so.superEggDrop(k,n)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1_2(self):
        test(self,   1,  2, 2)

    def test_2_1(self):
        test(self,  2, 1, 1)

    def test_2_2(self):
        test(self,  2, 2, 2)

    def test_2_3(self):
        test(self, 2,  3, 2)

    def test_2_4(self):
        test(self, 2,  4, 3)

    def test_2_5(self):
        test(self, 2,5, 3)

    def test_2_10(self):
        test(self, 2,  10, 4)

    def test_2_99(self):
        test(self,  2, 100, 14)

    def test_2_100(self):
        test(self,  2, 100, 14)
    
    def test_2_101(self):
        test(self,  2, 101, 14)

    def test_2_345(self):
        test(self,  2, 345, 26)

    def test_2_999(self):
        test(self, 2,  999, 45)

    def test_2_1000(self):
        test(self,  2, 1000, 45)

    def test_3_1(self):
        test(self,   3,  1, 1)
    
    def test_3_2(self):
        test(self,   3,  2, 2)
    
    def test_3_3(self):
        test(self,   3,  3, 2)
    
    def test_3_4(self):
        test(self,   3,  4, 3)
    
    def test_3_5(self):
        test(self,   3,  5, 3)
    
    def test_3_6(self):
        test(self,   3,  6, 3)
    
    def test_3_7(self):
        test(self,   3,  7, 3)
    
    def test_3_14(self):
        test(self,   3,  14, 4)
    
    def test_3_100(self):
        test(self,   3,  100, 9)
    
    def test_3_200(self):
        test(self,   3,  200, 11)
    
    def test_3_1000(self):
        test(self,   3,  1000, 19)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 3374 ms, faster than 9.20% of Python3 online submissions for Super Egg Drop.
Memory Usage: 14.4 MB, less than 74.30% of Python3 online submissions for Super Egg Drop.
'''

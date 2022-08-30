from heapq import heappop, heappush
import unittest
from typing import List, Optional, Dict, Set
from math import sqrt
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        if n == 1:
            return -1

        nums.sort()
        ans = -1
        left  = 0
        right = 1
        while right+1<n and nums[left] + nums[right+1] < k:
            right+=1
        
        while left < right:
            cur = nums[left] + nums[right]
            if cur==k-1:
                return cur
            elif cur<k:
                ans = max(ans, cur)
                left += 1
            else:
                right -= 1
            
        return ans


def test(testObj: unittest.TestCase, nums: List[int], k: int, expected:int) -> None:
    
    so = Solution()
    actual = so.twoSumLessThanK(nums,k)
    testObj.assertEqual(actual, expected)
        

class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [34,23,1,24,75,33,54,8],  60, 58)

    def test_2(self):
        test(self,   [10,20,30],  15, -1)
    
    def test_3(self):
        test(self, 
            [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944],
            200, 198)
    
    def test_4(self):
        test(self, 
            [803,468,292,154,924,424,197,277,753,86,984,144,105,450,287,265,655,404,407,794,513,976,241,272,84,503,65,654,805,413,362,907,297,473,113,567,646,607,806,674,424,753,870,574,765,170,603,696,513,58],
            300, 299)
    
    def test_5(self):
        test(self, 
            [5,5,5], 15, 10)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 47 ms, faster than 91.11% of Python3 online submissions for Two Sum Less Than K.
Memory Usage: 13.9 MB, less than 26.08% of Python3 online submissions for Two Sum Less Than K.
'''

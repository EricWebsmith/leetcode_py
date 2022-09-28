from bisect import bisect_left
import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None


def get_left_increase_dp(nums):
        n = len(nums)
        left = [nums[0]]
        dp_left = [1]
        for i in range(1, n):
            if nums[i]>left[-1]:
                left.append(nums[i])            
            else:
                index = bisect_left(left, nums[i])
                if left[index] > nums[i]:
                    left[index] = nums[i]

            dp_left.append(len(left))
        return dp_left


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp_left = get_left_increase_dp(nums)
        nums.reverse()
        dp_right = get_left_increase_dp(nums)
        dp_right.reverse()

        best = 0
        for i in range(1, n-1):
            if dp_left[i]>1 and dp_right[i]>1:
                best = max(best, dp_left[i]+dp_right[i] - 1)
        
        return n - best


def test(testObj: unittest.TestCase, nums: List[int], expected:List[int]) -> None:
    so = Solution()
    actual = so.minimumMountainRemovals(nums)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,3,1], 0)

    def test_2(self):
        test(self,   [2,1,1,5,6,2,3,1], 3)
    
    def test_3(self):
        test(self,   [4,3,2,1,1,2,3,1], 4)
    
    def test_4(self):
        test(self,   [9,8,1,7,6,5,4,3,2,1], 2)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 107 ms, faster than 98.33% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
Memory Usage: 14.2 MB, less than 57.74% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
'''

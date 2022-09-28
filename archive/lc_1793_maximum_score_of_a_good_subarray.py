import unittest
from typing import List
from data_structure.binary_tree import TreeNode, array_to_treenode, treenode_to_array
from data_structure.nary_tree import Node, array_to_node, node_to_array
null = None

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[k] = nums[k]
        for i in range(k-1, -1, -1):
            dp[i] = min(nums[i], dp[i+1])

        for i in range(k+1, n):
            dp[i] = min(nums[i], dp[i-1])

        left  = 0
        right = n - 1
        ans = min(dp[left], dp[right]) * (right - left + 1)
        while left<right:
            if dp[left] < dp[right]:
                t = dp[left] * (right - left + 1)
                ans = max(t, ans)
                while left<n-1 and dp[left+1]==dp[left]:
                    left +=1
                left += 1
            else:
                t = dp[right] * (right - left + 1)
                ans = max(t, ans)
                while right>0 and dp[right-1] == dp[right]:
                    right -= 1
                right -= 1

        return ans



def test(testObj: unittest.TestCase, nums: List[int], k: int, expected:int) -> None:
    
    so = Solution()
    
    actual = so.maximumScore(nums,k)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [1,4,3,7,4,5],  3, 15)

    def test_2(self):
        test(self,   [5,5,4,5,4,1,1,1],  0, 20)
    
    def test_3(self):
        test(self,   [5],  0, 5)
    
    def test_4(self):
        test(self,   [5, 5],  0, 10)
    
    def test_5(self):
        test(self,   [2, 5, 2],  1, 6)
    
    def test_6(self):
        test(self,   [2, 2, 2],  1, 6)
    
    def test_7(self):
        test(self,   [2, 2, 3, 2, 1],  1, 8)
    

if __name__ == '__main__':
    unittest.main()

'''
Runtime: 1195 ms, faster than 98.10% of Python3 online submissions for Maximum Score of a Good Subarray.
Memory Usage: 25.2 MB, less than 21.67% of Python3 online submissions for Maximum Score of a Good Subarray.
'''

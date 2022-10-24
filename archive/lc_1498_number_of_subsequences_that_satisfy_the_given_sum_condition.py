
import unittest
from typing import List
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = int(1e9+7)
        n = len(nums)
        nums.sort()
        ans:int = 0
        i = 0
        j = n - 1
        while i<=j:
            if nums[i]+nums[j]>target:
                j -= 1
            else:
                ans += pow(2, j-i, mod)
                i += 1

        return ans % mod


def test(testObj: unittest.TestCase, nums: List[int], target: int, expected:int) -> None:
    
    s = Solution()
    actual = s.numSubseq(nums,target)
    testObj.assertEqual(actual, expected)
        

class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        test(self,  [3,5,6,7],  9, 4)

    def test_2(self):
        test(self,  [3,3,6,8],  10, 6)

    def test_3(self):
        test(self,  [2,3,3,4,6,7],  12, 61)
    

if __name__ == '__main__':
    unittest.main()
        

"""
Runtime: 868 ms, faster than 88.95% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
Memory Usage: 26.9 MB, less than 10.48% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
"""
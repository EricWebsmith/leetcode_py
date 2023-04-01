import unittest
from bisect import bisect_left

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        index = bisect_left(nums, target)
        if index < len(nums)  and nums[index] == target:
            return index
        
        return -1


def test(testObj: unittest.TestCase, nums: list[int], target: int, expected: int) -> None:
    so = Solution()
    actual = so.search(nums, target)
    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):
    
    def test_1(self):
        test(self,   [-1,0,3,5,9,12],  9, 4)

    def test_2(self):
        test(self,   [-1,0,3,5,9,12],  2, -1)


if __name__ == '__main__':
    unittest.main()


'''
Runtime
236 ms
Beats
88.33%
'''

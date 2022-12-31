
import unittest
from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        operated = float('-inf')
        unoperated = float('-inf')
        maxS = float('-inf')
        for num in nums:
            operated = max(operated+num, unoperated + num**2, num**2)
            unoperated = max(num, unoperated + num)
            maxS = max(operated, maxS)

        return maxS


def test(testObj: unittest.TestCase, courses: List[List[int]], expected: int) -> None:
    s = Solution()
    actual = s.maxSumAfterOperation(courses)
    testObj.assertEqual(actual, expected)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        test(self,  [2, -1, -4, -3], 17)

    def test_2(self):
        test(self,  [1, -1, 1, 1, -1, -1, 1], 4)


if __name__ == '__main__':
    unittest.main()

'''
Runtime
1407 ms
Beats
66.67%
'''

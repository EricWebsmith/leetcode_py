import unittest
from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [-1]
        if n == 2:
            return [-1, -1]
        stack = []
        numk = nums[-2]
        numj = nums[-1]
        ans = [-1] * n
        for i in range(n-3, -1, -1):
            if nums[i] < numk and nums[i] < numj:
                ans[i] = numj
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
            elif nums[i] < numk or nums[i] < numj:
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1]
            else:
                count = 0
                index = -1
                if stack and stack[-1] > nums[i]:
                    count = 1
                while count < 2 and stack and index > -len(stack):
                    index -= 1
                    if stack[index] > nums[i]:
                        count += 1

                if stack and count == 2:
                    ans[i] = stack[index]

            stack.append(numj)
            numj = numk
            numk = nums[i]

        return ans


def test(testObj: unittest.TestCase, nums: List[int], expected: List[int]) -> None:

    so = Solution()

    actual = so.secondGreaterElement(nums)

    testObj.assertEqual(actual, expected)


class TestClass(unittest.TestCase):

    def test_1(self):
        test(self,   [2, 4, 0, 9, 6], [9, 6, 6, -1, -1])

    def test_2(self):
        test(self,   [3, 3], [-1, -1])

    def test_3(self):
        test(self,   [1, 17, 18, 0, 18, 10, 20, 0],
             [18, 18, -1, 10, -1, -1, -1, -1])

    def test_4(self):
        test(self,  [11, 13, 15, 12, 0, 15, 12, 11, 9],
             [15, 15, -1, -1, 12, -1, -1, -1, -1])

    def test_5(self):
        test(self,  [1],
             [-1])

    def test_6(self):
        test(self,  [1, 2],
             [-1, -1])

    def test_7(self):
        test(self,  [1, 2, 3],
             [3, -1, -1])


if __name__ == '__main__':
    unittest.main()

'''

'''
